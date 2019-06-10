# TODO:

### Role:
* nas storage / samba share (Playbook)
* add a role to install java / openjdk (Playbook)
### Task:
* extend the default template to allow configuration like the ones deffied in templates/parts/mediawiki.locaiton (webservices)
* add cron block, currently commented out and in sample doc (webservices)
* create lets encrypt certificate and enable in config /etc/postfix/main.cf (postfix)
* add parameter option to disable bayesian learning -  (spamassassin)
### Improvement:
* add feature to keep /etc/ngins/sites-enabled clean based on webservices_exclusive_nginx config (webservices)
* make use of option webservices_exclusive_nginx to identify and delete not used configurations (webservices)
* if all nginx sites are disabled, add the default config (webservices)
* Delete ( maybe even revoke) let's encrypt certifiactes if no longer in use (webservices)
* when deactivating mysql don't delete the DB only the user, use global enable to delete DB (webservices)
* add slack integration https://peteris.rocks/blog/monit-configuration-with-slack/ (monit)
* improve pybackup and add it to PIP, then install using pip - rename (pybackup)
* add fai2ban for postfix and imap login attempts (fail2ban)
* add automatic system update with cron (basic_host)
* delete gitea database on deactivation (gitea)
* add email ssl server validation like: https://blogging.dragon.org.uk/testing-imap-mailserver/ -  (validation)
* add validation for sftp login, private key on secret? (validation)
* add report for password login users? (validation)
* add report for lets encrypt dry-renew - name: Validate sftp configuration (validation)
* change package behaviour similar to files with package: <status> [ present | absent | purged] (validation)
### Check:
* htpasswd_filename generation (webservices)
### Verify:
* check if rather add webserive user to www-data or add www-data to webservice group (webservices)
* check compatibility level of postfix /etc/postfix/main.cf (postfix)
* make sure that the php worker logs are being rotated, maybe need to create a group and add the workers to the group (php-fpm)
### Refactor:
* move all certbot like cron renew to this role and, (letsencrypt)
### Verification:
* check if pre-create backup dir is really needed -  (pybackup)
### Blocker:
* delete after 6 months rule (dovecot)
### Validation:
* add a validation to determine if the domain is properly resolved to 127.0.0.1 ( needed for parsoid) (mediawiki)
### Bug:
* some file permisions are root:root after download + install, ============================================================================================================ Visual Editor / Parsoid ============================================================================================================ (mediawiki)
* the server group is hardcored to "server", needs to be iterable -  (validation)
* the packages validation currently performs changes, but it should only check (validation)
### Update:
* update gitea binary data (gitea)
* update roundcube to latest version (roundcube)
### Deprecation:
* remove old spamlearn actions (spamassassin)

Documentation generated using: [Ansible-autodoc](https://github.com/AndresBott/ansible-autodoc)