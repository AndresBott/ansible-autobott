# Ansible Role: postfix

Ansible role to install and configure postfix 

## Tags:

* `role_postfix` - Flag to run only this role

## Variables:

* `run_role_postfix`: `yes` - flag to disable the role



* `postfix_postgrey`: `no` - Install and configure postgrey greylisting



* `postfix_postgrey_port`: `10023` - Port for postgrey to listen to



* `postfix_postgrey_delay`: `60` - the graylisting delay in seconds



* `postfix_max_mail_size`: `10240000` - The maximal size in bytes of a message, including envelope information.


## TODO:

#### Verify:
* check compatibility level of postfix /etc/postfix/main.cf 
* check if letsencrypt certificate domains are correctly defined, k9 mail seems to fail 
#### Task:
* create lets encrypt certificate and enable in config /etc/postfix/main.cf 

## Author Information
This role:  was created by: Andres bott <contact@andresbott.com>

Documentation generated using: [Ansible-autodoc](https://github.com/AndresBott/ansible-autodoc)

