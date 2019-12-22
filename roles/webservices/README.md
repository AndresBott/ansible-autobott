# Ansible Role: webservices

Ansible role to maintain nginx based webservices, this role glues together all other webservice roles in ansible-autobott project

## Actions:

Actions performed by this role


* create/delete users, and their corresponding home structure 
* create/delete nginx configurations for every domain 
* create/delete php-fpm pool configurations for every domain 
* create/delete mysql databases and related users for every service 
* create ssl certificates for every domain (self signed or let's encrypt) 
* create sample dummy content if enabled by configuration 
* create cron entries for configured actions 


## Tags:

* `webservices` - run all webservices actions


* `webservices_users` - update the settings for webservices users


* `webservices_nginx` - update the nginx settings for webservices


* `webservices_phpfpm` - update the php-fom settings for webservices


* `webservices_mysql` - update the mysql settings for webservices ( only when run_role_mysql:yes )


* `webservices_ssl` - update the ssl / let's Encrypt certificates for webservices


* `webservices_sample_content` - create sample content if it does not exists


* `webservices_cron` - create cron entries

## Variables:

* `webservices_root`: `"/vhosts"` - root dir for all webservices (immutable)



* `webservices_group`: `www-data` - default group for the http server (apache/nginx)



* `webservices_letsencrypt_renew_email`: `no` - email address to send letsencrypt email renewals



* `webservices_exclusive_nginx`: `true` - (not implemented) if set to true, we assume that all configurations in /etc/nginx/sites-* are managed by this ansible role, any configuration file not defined in webservices will be deleted



* `webservices`: `[]` - define and configure all the webservices

example: 


```yaml
webservices:
  - name: demons_run                      # (mandatory) use simple names (no dots, special chars)
    enabled: yes                          # (mandatory) WARNING: changing this to no will delete your data
    uid: 1002                             # (mandatory) uid for the system user to be created
    shell: "/bin/false"                   # allow shell for that user
    ssh_key:                              # allow ssh login using ssh keys (multi-value)
      - "ssh-rsa AAAAA.... john@laptop"
    groups: []                            # add this web-services user to a specific group
    password: "clear-text"                # add a password (cleartext, encrypted later) , set to 'no' (false) to disable password login
    sample_content: no                    # add sample landing page, accepted values: no, "html", "php", useful as dummy content
#=
    nginx: # remove domains to disable
      enabled: yes                        # (mandatory) allows to disable the service without deleting the content
      servers:                            # (mandatory) list of associated nginx configs for this service
          #=
        - domain: demons-run.localhost    # (mandatory) domain name to listen to
          add_fqdn_subdomain: no          # if set to yes and the server FQDN is not the listen domain, then add also domain.fqdn to server listen
          subdomain_wildcard: no          # if set to yes, listen to *.domain
          template: default               # (mandatory) use different nginx templates:
                                             default - default for php and static content
                                             proxy - proxy template
                                             proxy_minio - modified proxy template to allow http auth on buckets using authentication_paths without conflicting with minio auth methods
          # port listen
          port: ""                        # define listen port for http, "" for default 80
          port_ssl: ""                    # define listen port for https, "" for default 443
          default_server: no              # is this the nginx default server
          # http proxy settings
          proxy_port: 5232                # proxy port to listen to, i.e 127.0.0.0:<port>
          proxy_lines:                  # add aditional lines in the proxy settings like:
            - "proxy_set_header X-Remote-User $remote_user"
            - "proxy_http_version 1.1"
            - "proxy_set_header Upgrade $http_upgrade"
            - 'proxy_set_header Connection "Upgrade"'
          # redirection
          redirect: no                    # no | "domain" add a domain to redirect to
          redirect_temp: no               # set to yes to use a temp 302 redirect, default is 301
          # logs
          log_access: yes                 # enable access log in /var/log/nginx/
          log_errors: yes                 # enable error log in /var/log/nginx/
          # document root
          document_root: "default"        # set the root dir for nginx relative to home_dir, "default" will be public_html
          #authentication
          authentication: no              # no to disable | yes to use a htpasswd file with users and pass
          authentication_paths: []        # apply authentication only to some paths, if empty it applies to /
          htpasswd_filename: no           # specify htpasswd file name, if set to 'no' it will be .htpasswd_<name>
          htpasswd_file_users:            # list of user:password, generated with "htpasswd -b -n <user1> <1234>"
            - user: user1
              pass: 1234
              enabled: yes
            - user: user2
              pass: 1234
              enabled: yes
          # letsencrypt ssl
          ssl:                             # (mandatory) if using ssl
            type: "optional"                      # no (disabled) | "optional" (allow http and https) | force (redirect http to https)
            provider: "selfsigned"                # type of certificate "selfsigned" for self signed | "letsencrypt" for acme letsnecrypt
            letsencrypt_notifications_email: "bla@bla.com"   # mandatory email used when generating let's encrypt certificates
            staging: yes                           # user let's encrypt staging server
            redirect_type: 301                    # type of http to https redirection if ssl is force
          #=
        - domain: demons2-run.localhost    # domain name to listen to
          ... # add multiple domains here
    php:
      enabled: yes                        # set to 'no' to don't have a php worker
      pm: "ondemand"                      # select the process manager: static, dynamic, ondemand
      pm_max_children: 10                 # maximum amount of child processes, this has an impact on ram
      pm_start_servers: 2                 # amount of start child processes
      pm_min_spare_servers: no            # lower end of child processes, only applied to "dynamic"
      pm_max_spare_servers: no            # higher end of child processes, only applied to "dynamic"
      pm_max_requests: 5000               # amount of requests handled by a child before killing it an spawning a new one
      pm_process_idle_timeout: 30s        # time a child process has to be idle before being killed
      error_reporting: "default"          # change the error log level according to php config string, set to "default" for : E_ALL & ~E_NOTICE & ~E_STRICT & ~E_DEPRECATED
      open_basedir: []                    # list of additional dirs where php has access to
#=
    mysql:
      enabled: no                         # WARNING: if you disable this the database will be deleted
      user: "default"                     # (mandatory) database user, if set to "default" uses webservice name
      password: "LpZPf55us9k03L"          # (mandatory) login password
      db_name: "default"                  # (mandatory) database name, if set to "default" uses webservice name
      collation: "default"                # define the sql collation, if set to "default" : utf8_general_ci is used
      encoding: "default"                 # define the character encoding, "default" is: utf8
#=
    cron_actions:
      - name: "run som maintainance"      # identification string
        enabled: no                       # se to no to don't run the cron job
        minute: "*/30"                    # minute component of the cron expression
        hour: "*"                         # hour component of the cron expression
        day: "*"                          # day component of the cron expression
        weekday: "*"                      # weekday component of the cron expression
        month:  "*"                       # month component of the cron expression
        user: "{{ webservice.name }}"     # user for the cron
        job: "/usr/bin/php"               # the action for the cron to do
#=
```
## TODO:

#### Task:
* extend the default template to allow configuration like the ones deffied in templates/parts/mediawiki.locaiton 
* add cron block, currently commented out and in sample doc 
#### Improvement:
* add feature to keep /etc/ngins/sites-enabled clean based on webservices_exclusive_nginx config 
* add sub_template to nginx in order to load application specific location rules, i.e roundcube block /cache 
* make use of option webservices_exclusive_nginx to identify and delete not used configurations 
* if all nginx sites are disabled, add the default config 
* Delete ( maybe even revoke) let's encrypt certifiactes if no longer in use 
* when deactivating mysql don't delete the DB only the user, use global enable to delete DB 
#### Check:
* htpasswd_filename generation 
#### Verify:
* check if rather add webserive user to www-data or add www-data to webservice group 

## Author Information
This role:  was created by: Andres bott <contact@andresbott.com>

Documentation generated using: [Ansible-autodoc](https://github.com/AndresBott/ansible-autodoc)

