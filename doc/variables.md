# Variables:

### Parsoid:
* `run_role_parsoid`: `yes` - flag to disable the role
* `parsoid_services`: `[]` - list of different services that will connect to this parsoid instance
example: 


```yaml
parsoid_services:
  - name: wiki1     # used to identify the different wiki installations
    api_uri:        # url to listen to
    namespace:      # the mediawiki namespace (domain)
```
* `parsoid_port`: `8142` - parsoind port
* `parsoid_bind_ip`: `'127.0.0.1'` - parsoind listen ip address
### Webservices:
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
          template: default               # (mandatory) use different nginx templates: default | proxy
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
### Opendkim:
* `run_role_opendkim`: `yes` - flag to disable the role
* `opendkim_signature_bits`: `1024` - encryption length: [1024 / 2048] this depends on your needs
* `opendkim_socket`: `"unix"` - type of socket: "unix" for unix socket | "inet" for http
* `opendkim_port`: `54321` - port used when using inet
* `opendkim_socket_location`: `"/var/spool/postfix/opendkim/opendkim.sock"` - location of the socket if type unix, autobott postfix expects this location.
### Mysql:
* `run_role_mysql`: `yes` - flag to run this role
* `mysql_root_username`: `root` - The default root user installed by mysql - almost always root
* `mysql_root_home`: `/root` - home of root user
* `mysql_root_password`: `""` - myqsl root  password
* `mysql_port`: `"3306"` - port where mysqld is listening
* `mysql_bind_address`: `'127.0.0.1'` - ip addresses mysqld is listening
* `mysql_skip_name_resolve`: `no` - if turned on, domain names will not be resolved i.e grants need to be done based on ip, increases performance
* `mysql_datadir`: `/var/lib/mysql` - location of the data of mysql, if you change might not work due to apparmor and similar
* `mysql_socket`: `/var/run/mysqld/mysqld.sock` - location of the unix socket, default value depends on OS mysql_socket: /var/run/mysqld/mysqld.sock
* `mysql_pid_file`: `/var/run/mysqld/mysqld.pid` - location of the PID file, default value depends on OS mysql_pid_file: /var/run/mysqld/mysqld.pid
* `mysql_general_log`: `""` - mysql log output file location i.e /var/log/mysql/mysql.log OR if set to 'syslog' it will log to syslog with the tag defined in mysql_syslog_tag, set to empty string to disable.
* `mysql_error_log`: `/var/log/mysql/error.log` - mysql error log output file location OR if set to 'syslog' it will log to syslog with the tag defined in mysql_syslog_tag, set to empty string to disable, default value depends on OS mysql_error_log: /var/log/mysql/error.log
* `mysql_syslog_tag`: `mysql` - if logging to syslog, this tag is used
* `mysql_slow_query_log_enabled`: `no` - enable logging for slow queries
* `mysql_slow_query_time`: `5` - log queries that take longer than X seconds
* `mysql_slow_query_log_file`: `/var/log/mysql-slow-query.log` - logfile for slow queries, default value depends on OS mysql_slow_query_log_file: /var/log/mysql-slow-query.log
* `mysql_key_buffer_size`: `"256M"` - memory optimization value
* `mysql_max_allowed_packet`: `"64M"` - memory optimization value
* `mysql_table_open_cache`: `"256"` - memory optimization value
* `mysql_sort_buffer_size`: `"1M"` - memory optimization value
* `mysql_read_buffer_size`: `"1M"` - memory optimization value
* `mysql_read_rnd_buffer_size`: `"4M"` - memory optimization value
* `mysql_myisam_sort_buffer_size`: `"64M"` - memory optimization value
* `mysql_max_connections`: `"151"` - memory optimization value
* `mysql_tmp_table_size`: `"16M"` - memory optimization value
* `mysql_max_heap_table_size`: `"16M"` - memory optimization value
* `mysql_query_cache_size`: `"16M"` - memory optimization value
* `mysql_query_cache_limit`: `"1M"` - memory optimization value
* `mysql_thread_cache_size`: `"8"` - memory optimization value
* `mysql_wait_timeout`: `"28800"` - The number of seconds the server waits for activity on a noninteractive connection before closing it.
* `mysql_lower_case_table_names`: `0` - If set to 1, table names are stored in lowercase, if set to 0 table names are case-sensitive.
* `mysql_supports_innodb_large_prefix`: `true` - require MySQL > 5.5. value defined depending on OS
* `mysql_innodb_large_prefix`: `"1"` - enable innodb_large_prefix
* `mysql_innodb_file_format`: `"barracuda"` - set the innodb_file_format
* `mysql_innodb_file_per_table`: `"1"` - 
* `mysql_innodb_buffer_pool_size`: `"256M"` - Set up to 80% of RAM but beware of setting too high.
* `mysql_innodb_log_file_size`: `"64M"` - Set to 25% of buffer pool size.
* `mysql_innodb_log_buffer_size`: `"8M"` - 
* `mysql_innodb_flush_log_at_trx_commit`: `"1"` - 
* `mysql_innodb_lock_wait_timeout`: `"50"` - 
* `mysql_mysqldump_max_allowed_packet`: `"64M"` - Maximum packet length to send to or receive from server
* `mysql_databases`: `[]` - Ensure mysql databases exist
example: 


```yaml
mysql_databases:
  - name: example
    collation: utf8_general_ci
    encoding: utf8
```
* `mysql_users`: `[]` - Ensure mysql users
example: 


```yaml
mysql_users:
  - name: example
    host: 127.0.0.1
    password: secret
    priv: *.*:USAGE
```
### Postfix:
* `run_role_postfix`: `yes` - flag to disable the role
* `postfix_db_name`: `vmail` - mysql database name
* `postfix_db_host`: `127.0.0.1` - mysql database host/ip
* `postfix_db_user`: `vmail` - mysql user
* `postfix_db_pass`: `"vmail"` - mysql password
* `postfix_data_dir`: `/vmails` - data directory that is shared between dovecot and postfix
* `postfix_max_mail_size`: `10240000` - The maximal size in bytes of a message, including envelope information.
### Node-red:
* `run_role_nodered`: `yes` - flag to disable the role
* `nodered_user`: `nodered` - system user
* `nodered_uid`: `no` - define a uid for the user
* `nodered_group`: `nodered` - system group
* `nodered_gid`: `no` - define a gid for the group
* `nodered_dir`: `/opt/nodered` - installation dir
* `nodered_service_name`: `nodered` - systemd service name
* `nodered_port`: `9663` - port to start node-red
* `nodered_pacakges`: `[node-red,node-red-dashboard]` - node-red packages (not needed to change)
### Monit:
* `run_role_monit`: `yes` - Flag to disable the role
* `monit_port`: `2812` - monit port
* `monit_httpd`: `no` - enable httpd server for monitoring and querying data
* `monit_interval`: `120` - services check interval
* `monit_initial_delay`: `120` - initial delay of checks in seconds, note web interface will also not be available
* `monit_alert`: `{...}` - configure email to send notifications
example: 


```yaml
monit_alert:
    notify: [] # emails to notify
    replyto: "reply@emai.com"
    smtp:
      url: "" # empty string to disable
      port: 587
      username: email@mail.com
      password: sompassword
      tls: yes
```
* `monit_checks`: `[]` - Configure the different checks monit will perform
example: 


```yaml
monit_checks: []
  - name: mysql
    enabled: yes
    type: process
    pid: "/var/run/mysqld/mysqld.pid"
    regex: "mysql"
    start: "/etc/init.d/mysql start"
    stop: "/etc/init.d/mysql stop"
    restart: "/etc/init.d/mysql restart"
    restart_tolerancy: 2
    additional_conditions: []
    additional_raw: "" #see samples in /etc/monit/conf-available
```
### Pybackup:
* `run_role_pybackup`: `yes` - flag to run this role
* `run_role_pybackup_remote`: `yes` - flag to run the remote backup feature
* `pybackup_jobs`: `[]` - list of backup jobs
example: 


```yaml
pybackup_jobs:
  - name: gitea          # job name
    backup_dir: /vhosts/gitea/home_dir/gitea   # directory that will be backed up
    follow_symlinks: yes # follows sym links when running backup
    output_dir: /vhosts/gitea/backups # directory the backup files will be put, WARNING use only one exclusive directory per job
    tmp_dir: ""          # relative or absolute tmp dir for backup operations, WARN the folder will be deleted on finish
    backup_mysql: gitea  # database name to backup
    keep_old: 4          # amount of older backups to keep
    file_owner: gitea    # change the ownership of the compressed backup file
    file_mode: "0700"    # change the mode of the compressed backup file
    cron:
      enabled: yes
      minute: "0"
      hour: "3"
      day_of_month: "1"
      day_of_week: "*"
      month: "*"
    remote: no           # perform a remote backup of this job when running tag: role_pybackup_remote
```
* `pybackup_remote_tmp`: `/tmp` - tmp location where the files will be copied during remote backup
* `pybackup_remote_fetch_type`: `"ans"` - mechanism used to fetch the file from the remote server, "ans" will use ansible module fetch | "scp" wil use ssh scp
* `pybackup_remote_out`: `"{{ playbook_dir }}/remote_backup"` - local directory where the remote backup will be stored you can pass this variable to the playbook as: --extra-vars "pybackup_remote_out=/home/ans"
### Fail2ban:
* `run_role_fail2ban`: `yes` - 
### Dovecot:
* `run_role_dovecot`: `yes` - flag to disable the role
* `dovecot_quota_enabled`: `yes` - enable dovecot quotas
* `dovecot_virtual_folders`: `[ 'All Mails', 'Flagged' ]` - enable custom virtual folders by providing an array of filters, current values: ['All Mails', 'Flagged']; set to no to disable
* `dovecot_postmaster_email`: `""` - define the default postmaster (server owner) email address for this server
### Basic_host:
* `basic_host_user`: `ans` - username for ansible login user
* `basic_host_uid`: `900` - uid for ansible login user
* `basic_host_group`: `ans` - group for ansible login user
* `basic_host_gid`: `900` - gid for ansible login user
* `basic_host_home`: `/home/ans` - home dir for ansible login user
* `basic_host_root_bashrc`: `true` - create a custom .brashrc for root user
* `basic_host_ssh_keys`: `[]` - User keys allowed to login as ansible admin, thus run ansible playbook
* `basic_host_ssh_keys_revoked`: `[]` - User keys that are no longer allowed to login as ansible admin
* `basic_host_sources_distro_country`: `ch` - select the country prefix for the distro template
* `basic_host_sources_d`: `[]` - additional sources to be added to /etc/apt/sources.list.d
* `basic_host_cache_valid_time`: `3600` - change the valid cache time of apt when running ansible multiple times
* `basic_host_installed_apps`: `[apt,ca-certificates]` - list of apps to be installed,
* `basic_host_extra_apps`: `[]` - second list of apps that can be defined
* `basic_host_hostname`: `""` - define the host's hostname
* `basic_host_fqdn`: `""` - define the host's Fully qualified domain name
* `basic_host_extra_host_entires`: `[]` - add extra entries to /etc/hosts
* `basic_host_cron_notification_mail`: `""` - enable cron to send emails to that address
* `basic_host_locale_to_be_generated`: `["en_US.UTF-8 UTF-8","es_ES.UTF-8 UTF-8"]` - list of locales to be generated (take care to use value from /usr/share/i18n/SUPPORTED,as locale-gen exit with code 0 even with errors...)
* `basic_host_locale_lang`: `en_US.UTF-8` - 
* `basic_host_locale_all`: `""` - 
* `basic_host_locale_language`: `""` - 
* `basic_host_locale_numeric`: `""` - 
* `basic_host_locale_time`: `""` - 
* `basic_host_locale_monetary`: `""` - 
* `basic_host_locale_paper`: `""` - 
* `basic_host_locale_identification`: `""` - 
* `basic_host_locale_name`: `""` - 
* `basic_host_locale_address`: `""` - 
* `basic_host_locale_telephone`: `""` - 
* `basic_host_locale_measurement`: `""` - 
* `basic_host_ssh_allow_passwd_login`: `no` - allow users to ssh using password
* `basic_host_ssh_allow_passwd_login_group`: `""` - if basic_host_ssh_allow_passwd_login is set to no, you can limit password ssh to certain group, set to empty string to disable
* `basic_host_ssh_sftp`: `yes` - enable sftp using openssh, see groups definitions to configure sftp jails
* `basic_host_ssh_X11forwarding`: `no` - enable X11 forwarding, this should not be needed on a normal server
* `basic_host_create_group_for_every_user`: `true` - Create a group for every user and make that their primary group
* `basic_host_users_group`: `users` - If we're not creating a per-user group, then this is the group all users belong to
* `basic_host_users_default_shell`: `/bin/bash` - default shell for created users
* `basic_host_users_create_homedirs`: `true` - Create home dirs for created users
* `basic_host_groups`: `[]` - List of groups to create
example: 


```yaml
basic_host_groups:
  - name: sftp
    gid: 402
    sftp_jail:
      enabled:  yes
      base_dir: "/home" #jail home dir: i.e /home/%u or /vhosts/%u
      allow_password: yes
      umask: "0077"
```
* `basic_host_system_users`: `[]` - List of system users to be created
example: 


```yaml
basic_host_system_users:
  - username: "tardis"
    name: "that blue box"
    groups: [ 'trenzalore','gallifrey']
    uid: 2001
    gid: 2001
```
* `basic_host_users`: `[]` - List of users to be added
example: 


```yaml
basic_host_users:
  - username: jdoe
    name: "The Doctor"
    groups: ['sudo', 'trenzalore','gallifrey']  # empty string removes user from all secondary groups
    uid: 2001
    gid: 2001 # optional
    password: "{{ secred_my_user_passwd | password_hash('sha512', 65534 | random(seed=inventory_hostname) | string) }}" # encrypted
    ssh_key:
      - "ssh-rsa AAAAA.... john@laptop"
      - "ssh-rsa AAAAB.... doctor@desktop"
    ssh_key_revoked: []
    shell: /bin/bash # optional
    home:  #commentout for default
    create_home: true
    home_is_sftp_jail: false
    bashrc: true #optional
```
* `basic_host_users_extra`: `[]` - second list of users to be added, this allows to define users at different locations
* `basic_host_users_deleted`: `[]` - list of users + user groups to NOT to be present. WARNING this will not delete their home
### Mediawiki:
* `run_role_mediawiki`: `yes` - flag used to disable this role
* `mediawiki_instances`: `[]` - list of different mediawiki installations, this allows you to run multiple wikis on one host
example: 


```yaml
mediawiki_instances:
  - name: wiki1                                     # used to identify the different wiki installations
    user: sample_wiki                               # system user to be used
    group: sample_wiki                              # system group to be used
    db_name: sample_wiki                            # database name
    db_user: sample_wiki                            # database user
    db_pass: "changeme"                             # database password
    install_dir: "/wiki/home_dir"                   # root installation dir
    public_html: "/wiki/home_dir/public_html"       # public available directory
    config:
      site_name: "sample wiki"                      # Name of the wiki site
      namespace: "sample_wiki"                      # used to differentiate the wikies in parsoid
      admin_user: "wiki"                            # wiki admin username (defined on installation)
      admin_pass: "changeme"                        # wiki admin password (defined on installation)
      base_url: "https://sample-wiki.localhost"     # full root domain of the wiki
      emergency_contact_mail: info@localhost.com    # emercenty contact email
      password_sender_mail: info@localhost.com      # password reset sender email
      locale: "en_US.utf8"                          # used for imagemagic, needs to be a valid locale
      lang: "en"                                    # Site language code, should be one of the list in ./languages/data/Names.php
      secret_key: "changeme"                        # secret key
      site_upgrade_key: "changeme"                  # used to turn on the web installer while LocalSettings.php is in place
      allowed_extensions:                           # allowed upload extensions
        - pdf
        - tiff
      whitelisted_extensions:                       # whitelist extensions that are normally not allowed
        - txt
        - js
      allow_js: no                                  # allow the upload of javascript files
      enable_visualeditor: yes                      # flag to enable visual editor and usage of parsoid (needed by visual editor)
      visualeditor_parsoid_bind_ip: 127.0.0.1       # parsoid server ip
      visualeditor_parsoid_bind_posrt: 7858         # parsoid server port
      enable_mobile_frontend: yes                   # enable mobile frontend theme
      enable_custom_css: yes                        # add a custom css with small changes (located in templates)
```
* `mediawiki_version`: `1.31.1` - current used versions
* `mediawiki_binary`: `"https://releases.wikimedia.org/mediawiki/1.31/mediawiki-1.31.1.tar.gz"` - current installation source
* `mediawiki_version_delete`: `["1.28.0"]` - installation versions to be deleted
* `mediawiki_VE_version`: `"REL1_31"` - current version of Visual editor to be installed
* `mediawiki_VE_binary`: `"https://extdist.wmflabs.org/dist/extensions/VisualEditor-REL1_31-6854ea0.tar.gz"` - current installation source
* `mediawiki_MFE_version`: `"REL1_31"` - current Mobile Frontend version to be installed
* `mediawiki_MFE_binary`: `"https://extdist.wmflabs.org/dist/extensions/MobileFrontend-REL1_31-7f66849.tar.gz"` - current installation source
### Radicale:
* `run_role_radicale`: `yes` - flag to disable the role
* `radicale_user`: `radicale` - service user
* `radicale_uid`: `no` - service uid, set to no to use system automatic
* `radicale_group`: `radicale` - service main group
* `radicale_gid`: `no` - service main gid, set to no to use system automatic
* `radicale_install_dir`: `/opt/radicale` - main installation location
* `radicale_data_dir`: `/opt/radicale/data` - data location
* `radicale_bound_ip`: `127.0.0.1` - service listen ip address
* `radicale_port`: `5232` - service port
### Composer:
* `run_role_composer`: `yes` - conditional used to disable this role, set to no to uninstall composer
### Gitea:
* `run_role_gitea`: `yes` - flag used to disable this role
* `gitea_bind_ip`: `"127.0.0.1"` - ip address to listen to
* `gitea_port`: `"3000"` - port to listen to
* `gitea_db_type`: `"mysql"` - database type: mysql or sqlite3
* `gitea_user`: `gitea` - system user
* `gitea_db_user`: `gitea` - mysql user and database name
* `gitea_db_pass`: `"gitea"` - mysql password
* `gitea_secret_key`: `"random"` - 
* `gitea_domain`: `"localhost"` - domain where gitea is installed, used for generating links
* `gitea_http_port`: `""` - if gitea is setup behind a proxy that is on a non standard port, change this to the termination port, used for url generation
* `gitea_version`: `1.2.2` - current installation version gitea_version: 1.2.2
* `gitea_binary`: `"https://github.com/go-gitea/gitea/releases/download/v{{gitea_version}}/gitea-{{gitea_version}}-linux-amd64"` - current download dir for the current version
* `gitea_sum`: `"2830d77004eb03865fa3860bfb4dd34ccd497070b6f6de667a7de97c3471e07d"` - checksum of the current version gitea_sum: "2830d77004eb03865fa3860bfb4dd34ccd497070b6f6de667a7de97c3471e07d"
example: **upgrade**

 in order to upgrade to a newer gitea version you need to setup all 3 variables accordingly
```yaml
gitea_version: 1.2.3
gitea_binary: "https://github.com/go-gitea/...."
gitea_sum: "2830d77 ... de97c3471e07d"
```
* `gitea_version_delete`: `["1.1.0"]` - dict of older versions that should be deleted
### Nginx:
* `nginx_pgks_to_install`: `[nginx,nginx-full]` - packages to be installed
* `nginx_user`: `www-data` - groupname for web services, this is default debian, don't change
* `nginx_worker_processes`: `2` - should be same as cpu count for best performance
* `nginx_worker_connections`: `1024` - max ammount of concurrent connections per worker
* `nginx_client_max_body_size`: `30m` - max size of a request body, i.e file upload + form data
* `nginx_default_error_page`: `""` - define path to a error page
* `nginx_modules`: `[]` - list of modules to be enabled
example: 


```yaml
nginx_modules:
  - mod-http-auth-pam.conf
  - mod-http-dav-ext.conf
  - mod-http-echo.conf
  - mod-http-geoip.conf
  - mod-http-image-filter.conf
  - mod-http-subs-filter.conf
  - mod-http-upstream-fair.conf
  - mod-http-xslt-filter.conf
  - mod-mail.conf
  - mod-stream.conf
```
### Nodejs:
* `run_role_nodejs`: `yes` - flag to disable the role
* `nodejs_version_repo`: `11 | {8,9,10,11}` - select the major version of nodejs you want to install; available versions based on https://github.com/nodesource/distributions/tree/master/deb
### Spamassassin:
* `run_role_spamassassin`: `yes` - flag to disable the role
* `spamassasin_required_score`: `2.5` - 
* `spamassasin_use_bayes`: `1` - enable bayesian filter
* `spamassasin_bayes_auto_learn`: `1` - enable bayesian auto learn
* `spamassasin_scores`: `[]` - disc of rules and weight values, see: http://spamassassin.apache.org/old/tests_3_3_x.html
example: 


```yaml
spamassasin_scores:
  DKIM_SIGNED: 1.0
  DKIM_VALID: -1.5
```
### Php-fpm:
* `run_role_php_fpm`: `yes` - flag to run the role php-fpm, set to no to uninstall php
* `php_output_buffering`: `4096` - ow much output data PHP should keep internally before pushing that data to the client see: http://php.net/output-bufferin
* `php_max_execution_time`: `30` - Maximum execution time of each script, in seconds
* `php_max_input_time`: `60` - Maximum amount of time each script may spend parsing request data.
* `php_memory_limit`: `128M` - Maximum amount of memory a script may consume (128MB)
* `php_error_reporting`: `E_ALL & ~E_DEPRECATED & ~E_STRICT` - Production Value = E_ALL & ~E_DEPRECATED & ~E_STRICT & ~E_STRICT, Development Value =  E_ALL,
* `php_display_errors`: `Off` - output errors to web browser, used in development
* `php_display_startup_errors`: `Off` - startup sequence are handled separately from display_errors
* `php_log_errors`: `On` - PHP can also log errors to locations such as a server-specific log
* `php_post_max_size`: `8M` - Maximum size of POST data that PHP will accept.
* `php_file_uploads`: `On` - Whether to allow HTTP file uploads.
* `php_upload_max_filesize`: `2M` - Maximum allowed size for uploaded files.
* `php_max_file_uploads`: `20` - Maximum number of files that can be uploaded via a single request
* `php_session_use_strict_mode`: `1` - Whether to use strict session mode. https://wiki.php.net/rfc/strict_sessions
* `php_session_name`: `SESSID` - Name of the session (used as cookie name).
* `php_opcache_enable`: `0` - Determines if Zend OPCache is enabled
* `php_opcache_memory_consumtion`: `128` - The OPcache shared memory storage size in MB
* `php_opcache_interned_strings_buffer`: `8` - The amount of memory for interned strings in Mbytes.
* `php_opcache_max_accelerated_files`: `1979` - The maximum number of keys (scripts) in the OPcache hash table, best values  { 223, 463, 983, 1979, 3907, 7963, 16229, 32531, 65407, 130987 }
* `php_opcache_max_wasted_percentage`: `5` - The maximum percentage of "wasted" memory until a restart is scheduled.
* `php_opcache_use_cwd`: `1` - append cwd to avoid collision to filenames
* `php_opcache_valiate_timestamps`: `1` - if enabled check for new scrips every revalidate_freq
* `php_opcache_revalidate_freq`: `2` - How often (in seconds) to check file timestamps for changes
* `php_opcache_revalidate_path`: `0` - reuse include_path files with the same name
* `php_opcache_save_comments`: `1` - disable to remove comments from saved code, may break apps that relay on comments, reduces size of opcodes
* `php_opcache_load_comments`: `1` - disable to remove comments from saved code, may break apps that relay on comments, reduces size of opcodes
* `php_opcache_fast_shutdown`: `1` - fast shutdown is used, without freezing allocated memory blocks
* `php_opcache_enable_file_override`: `0` - Allow file existence override, may increase performance, but risky
* `php_opcache_optimization_level`: `0xffffffff` - A bitmask, where each bit enables or disables the appropriate OPcache
* `php_opcache_max_file_size`: `4M` - Allows exclusion of large files from being cached. By default all files
* `php_opcache_consistency_checks`: `0` - Check the cache checksum each N requests, 0 means disabled
* `php_opcache_force_restart_timeout`: `180` - How long to wait (in seconds) for a scheduled restart to begin if the cache is not being accessed.
* `php_opcache_error_log`: `""` - error log file, Empty string assumes "stderr"
* `php_opcache_log_verbosity_level`: `1` - 0: fatal errors, 1: erros, 2 warning, 3 information,  4 debug.
* `php_opcache_preferred_memory_model`: `""` - Preferred Shared Memory back-end. Leave empty and let the system decide.
### Email-service:
* `run_email_service`: `yes` - flag to disable the role
* `email_data_dir`: `/vmails` - Root directory for email accounts and data
* `email_data_user`: `vmail` - email server username
* `email_data_uid`: `2000` - uid for username
* `email_data_group`: `vmail` - email server primary group
* `email_data_gid`: `2000` - gid for group
* `email_db_name`: `vmail` - mysql database name
* `email_db_host`: `127.0.0.1` - mysql database host/ip
* `email_db_user`: `vmail` - mysql user
* `email_db_pass`: `"vmail"` - mysql password
* `email_postmaster`: `"postmaster@{{ ansible_fqdn }}"` - email server postmaster emails
* `email_server_domain`: `mail.localhost` - email server main domain, the server can handle multiple domain email addresses but needs one primary domain for the clients to connect to.
* `email_subdomain`: `mail` - subdomain part of the domain
* `email_debug`: `no` - add some email debug into the configuration ( don't use in production)
* `email_cert_provider`: `""` - set to "letsencrypt" to use let's encrypt, any different string will use a self signed certificate or
* `email_domains`: `[]` - configuration of domain names the server will handle
example: 


```yaml
email_domains:
  - domain: localhost           # domain to add accounts
    description: "mail Server"  # description
    quota: ""                   # domain quota in Kb, disabled if ""
    active: yes                 # enable/disable all emails of a domain
```
* `email_accounts`: `[]` - configuration of email accounts handled by the server
example: 


```yaml
email_accounts:
  - email: main@localhost       # full email address, must contain @
    password: mail              # clear text password, you should store it in vault or similar
    name: "main email"          # email account owner name
    quota: 41943040             # account quota in Kb
    ham_folder: [".Archivados"] # ham learning folder
    spam_folder: [".Spam"]      # spam learning folder
    active: yes                 # enable/disable this email
```
* `email_alias`: `[]` - configuration of email aliases handled by the server
example: 


```yaml
email_alias:
  - address: postmaster@example.com  # alias address
    goto: main@localhost             # destination address
    active: yes                      # if the alias is active or not
```
### Roundcube:
* `run_role_roundcube`: `yes` - flag used to disable this role
* `roundcube_instances`: `[]` - list of roundcube instances that will be installed
example: 


```yaml
roundcube_instances:
  - name: webmail                                 # used to identify the different wiki installations
    user: roundcube                               # system user to be used
    group: roundcube                              # system group to be used
    db_name: roundcube                            # database name
    db_user: roundcube                            # database user
    db_pass: "changeme"                           # database password
    install_dir: "{{webservices_root}}/roundcube/home_dir" # root installation dir
    public_html: "{{webservices_root}}/roundcube/home_dir/public_html" # public available directory
    tmp_dir: "{{webservices_root}}/roundcube/home_dir/tmp"
    config:
      ignore_certificate_validation: yes           # this is needed for simple self signed certificates, and should no be used in production
      mail_server: "mail.localhost"
      cypher: "Quaba75eesdahfoh2eizay8i"           # excatly 24 chars
      plugins: []                                  # see <installdir>/plugins, these are provided with roundcube
      manual_plugins: []
```
* `roundcube_current_version`: `1.3.3` - roundcube version to install
* `roundcube_sources`: `` - roundcube installation candidates, this can be changed per configuration
example: 


```yaml
roundcube_sources:
  1.3.3:
    url: https://github.com/roundcube/roundcubemail/releases/download/1.3.3/roundcubemail-1.3.3-complete.tar.gz
    sum: "05d9856c966c0d93accabf724e7ff2fd493bba1a57c44247ed0a2aacd617c879"
```
* `roundcube_manual_plugins`: `<see examples >` - list of manual installable plugins, this can be extended per configuration.
example: 


```yaml
roundcube_manual_plugins:
    - name: gravatar
      url: https://github.com/prodrigestivill/roundcube-gravatar/archive/master.zip
      repo_name: roundcube-gravatar-master
      plugin_file: gravatar.php
      config_file: 20_roundcube/gravatar.config-inc.php.j2
       #====
    - name: authres_status
      url: https://github.com/pimlie/authres_status/archive/master.zip
      repo_name: authres_status-master
      plugin_file: authres_status.php
      config_file: 20_roundcube/authres_status.config-inc.php.j2
       #====
    - name: automatic_addressbook
      url: https://github.com/sblaisot/automatic_addressbook/archive/master.zip
      repo_name: automatic_addressbook-master
      plugin_file: automatic_addressbook.php
      config_file: 20_roundcube/automatic_addressbook.config-inc.php.j2
      include_post_install: 21_custom_roundcube_automatic_addressbook.yaml
       #====
    - name: automatic_addressbook_ng
      url: https://github.com/teonsystems/roundcube-plugin-automatic-addressbook-ng/archive/master.zip
      repo_name: roundcube-plugin-automatic-addressbook-ng-master
      plugin_file: automatic_addressbook_ng.php
      config_file: 20_roundcube/automatic_addressbook_ng.config.php.j2
       #====
    - name: carddav
#      url: https://github.com/blind-coder/rcmcarddav/releases/download/v2.0.4/carddav-2.0.4.zip
      url: https://github.com/blind-coder/rcmcarddav/releases/download/v3.0.2/carddav-3.0.2.zip
      repo_name: carddav
      plugin_file: carddav.php
      config_file: 20_roundcube/carddav.config-inc.php.j2
       #====
    - name: persistent_login
      url: https://github.com/AndresBott/persistent_login/archive/master.zip
      repo_name: persistent_login-master
      plugin_file: persistent_login.php
      config_file: 20_roundcube/persistent_login.config-inc.php.j2
      include_post_install: 21_custom_roundcube_persistent_login.yaml
       #====
    - name: melanie2_larry
      url: https://github.com/messagerie-melanie2/Roundcube-Plugin-Melanie2-Larry/archive/master.zip
      repo_name: Roundcube-Plugin-Melanie2-Larry-master
      plugin_file: melanie2_larry.php
       #====
    - name: mobile
      url: https://github.com/messagerie-melanie2/Roundcube-Plugin-Mobile/archive/master.zip
      repo_name: Roundcube-Plugin-Mobile-master
      plugin_file: mobile.php
      enable: no
       #====
    - name: jquery_mobile
      url: https://github.com/messagerie-melanie2/Roundcube-Plugin-JQuery-Mobile/archive/master.zip
      repo_name: Roundcube-Plugin-JQuery-Mobile-master
      plugin_file: jquery_mobile.php
      enable: no
```
### Validation:
* `run_role_validation`: `yes` - flag to disable the validation role
* `validation_packages_uninstall_group`: `[]` - list of packages to be uninstalled, define at group level
* `validation_packages_uninstall_host`: `[]` - list of packages to be uninstalled, define at host level
* `validation_packages_purge_group`: `[]` - list of packages to be purged, define at group level
* `validation_packages_purge_host`: `[]` - list of packages to be purged, define at host level
* `validation_files_group`: `[]` - validate a list of files on different conditions, see example
example: 


```yaml
validation_files_absent_host:
  - file: apache2
    path: "/etc/apache2/apache2.conf"
    condition:
    - absent                           # check for file to be absent
  - file: nginx
    path: "/etc/nginx/nginx.conf"
    condition:
    - present                          # check for file to be present
```
* `validation_files_absent_host`: `[]` - same as validation_files_absent_group but at to be defined at host level
* `validation_shell_group`: `[]` - validate a list of shell commands, see example
example: 


```yaml
validation_shell_group:
  - shell: php -v | head -1 | grep -o -P '\d+\.\d' # shell command to execute
    condition:
    - rc0                            # check for return code == 0
    - stdout: "7.0"                  # compare stdout string to value
```
* `validation_shell_host`: `[]` - same as validation_shell_group but at to be defined at host level
* `validation_http_group`: `[]` - validate a list of http requests, see example
example: 


```yaml
validation_http_host:
  - url: http://google.com
    condition:
    - rc: 200                        # check for return code == 200
    - rc: 302                        # check for return code == 302
    - header: "mediawiki_api_error"  # check if a header contains a certain value
      value: "readapidenied"
```
* `validation_http_host`: `[]` - same as validation_http_group but at to be defined at host level

Documentation generated using: [Ansible-autodoc](https://github.com/AndresBott/ansible-autodoc)