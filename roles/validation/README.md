# Ansible Role: validation

Perform configured validations at the end of the playbook run 

## Actions:

Actions performed by this role


* Packages - Take care of ensuring that defined packages are uninstalled 
* Files - Take care of ensuring that defined files are present or absent 
* Shell - run shell commands on the host and validated the result 
* Mysql - verify there are no users with empty password 


## Tags:

* `role_validation` - run validations


* `validation` - run validations


* `validation_packages` - run package validations


* `validation_files` - run file validations


* `validation_shell` - run shell validations


* `validation_http` - run http validations


* `validation_mysql` - run mysql validations


* `validation_email` - 

## Variables:

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
    method: "GET"                    # (optional) set the request method, if omitted GET is used
    validate_certs: no               # (optional) set to yes to fail request on invalid ssl certificate
    from_local_host: true            # if true, run the http request from the same machine as your ansible,
                                       if false, run from the remote machine
    http_auth_user: admin            # send http auth user, password is also required
    http_auth_password: admin        # send http auth password
    condition:
    - rc: 200                        # check for return code == 200
    - rc: 302                        # check for return code == 302
    - header: "mediawiki_api_error"  # check if a header contains a certain value
      value: "readapidenied"
```

* `validation_http_host`: `[]` - same as validation_http_group but at to be defined at host level


## TODO:

#### Bug:
* the server group is hardcored to "server", needs to be iterable -  
* the packages validation currently performs changes, but it should only check 
#### Improvement:
* add email ssl server validation like: https://blogging.dragon.org.uk/testing-imap-mailserver/ -  
* add validation for sftp login, private key on secret? 
* add report for password login users? 
* add report for lets encrypt dry-renew - name: Validate sftp configuration 
* change package behaviour similar to files with package: <status> [ present | absent | purged] 

## Author Information
This role:  was created by: Andres bott <contact@andresbott.com>

Documentation generated using: [Ansible-autodoc](https://github.com/AndresBott/ansible-autodoc)

