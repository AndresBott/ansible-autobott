# Tags:
### Playbook:
### Parsoid:
* `role_parsoid` - Flag to only run this roles
### Webservices:
* `webservices` - run all webservices actions
* `webservices_users` - update the settings for webservices users
* `webservices_nginx` - update the nginx settings for webservices
* `webservices_phpfpm` - update the php-fom settings for webservices
* `webservices_mysql` - update the mysql settings for webservices ( only when run_role_mysql:yes )
* `webservices_ssl` - update the ssl / let's Encrypt certificates for webservices
* `webservices_sample_content` - create sample content if it does not exists
* `webservices_cron` - create cron entries
### Opendkim:
* `role_opendkim` - Only run this role
* `role_opendkim_keys` - print current public keys
### Mysql:
* `role_mysql` - run only this role
### Postfix:
* `role_postfix` - Flag to run only this role
### Node-red:
* `role_nodered` - Flag to only run this roles
### Monit:
* `role_monit` - Only run the role monit
### Letsencrypt:
* `role_letsencrypt` - Flag to only run this role
### Pybackup:
* `role_pybackup` - flag to run only this role
* `role_pybackup_remote` - Run the remote backup action, this is only executed if the tag is provided.
### Fail2ban:
* `role_fail2ban` - Only run the role fail2ban
### Dovecot:
* `role_dovecot` - Only run this role
### Basic_host:
* `enroll` - run the the initial enrollment actions of the system
* `role_basic_host` - only run the role basichost
* `configuration` - run configuration tasks
* `upgrade` - perform a system upgrade
* `action_upgrade` - perform a system upgrade, same as upgrade
* `users` - update user definitions and credentials
### Mediawiki:
* `role_mediawiki` - Flag to only run this role
### Radicale:
* `role_radicale` - Flag to only run this roles
### Composer:
* `role_composer` - Only run the role php composer
### Gitea:
* `role_gitea` - Flag to only run this role
### Nginx:
* `role_nginx` - Only run the role nginx
### Nodejs:
* `role_nodejs` - Only run the role nodejs
### Spamassassin:
* `role_spamassassin` - Only run this role
### Php-fpm:
* `role_php_fpm` - run only php-fpm role
### Email-service:
* `email_service` - Only run this role
* `email_accounts` - only update email accounts, if there has been any change
* `role_dovecot` - 
### Roundcube:
* `role_roundcube` - Flag to only run this role
### Validation:
* `role_validation` - run validations
* `validation` - run validations
* `validation_packages` - run package validations
* `validation_files` - run file validations
* `validation_shell` - run shell validations
* `validation_http` - run http validations
* `validation_mysql` - run mysql validations

Documentation generated using: [Ansible-autodoc](https://github.com/AndresBott/ansible-autodoc)