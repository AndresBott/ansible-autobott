# Ansible Role: dovecot

Install and configure dovecot in ansible-autobott 

## Actions:

Actions performed by this role


* Install dovecot 
* configure dovecot in /etc/dovecot/conf.d/ 
* Configue sieve mail filtering 
* Configure dovecot virtual directories 
* configure dovecot quotas 


## Tags:

* `role_dovecot` - Only run this role

## Variables:

* `run_role_dovecot`: `yes` - flag to disable the role



* `dovecot_quota_enabled`: `yes` - enable dovecot quotas



* `dovecot_virtual_folders`: `[ 'All Mails', 'Flagged' ]` - enable custom virtual folders by providing an array of filters, current values: ['All Mails', 'Flagged']; set to no to disable



* `dovecot_mailbox_spam_expurge`: `60d` - after how many days emails in the spam folder will be deleted



* `dovecot_mailbox_autoexpunge`: `[]` - a set of mailboxes with different expunge values (delete after x days)

example: 


```yaml
- name: Guardar6meses
    days: 180
```
## TODO:

#### Blocker:
* delete after 6 months rule 

## Author Information
This role:  was created by: Andres bott <contact@andresbott.com>

Documentation generated using: [Ansible-autodoc](https://github.com/AndresBott/ansible-autodoc)

