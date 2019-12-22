# Ansible Role: letsencrypt

Ansible role to install the let's encrypt acme client 

## Tags:

* `role_letsencrypt` - Flag to only run this role

## Variables:

* `run_role_letsencrypt`: `yes` - flag to disable the role



* `letsencrypt_renew_hooks`: `[]` - list of hooks to add to cron after a certificate has been renewed

example: 


```yaml
letsencrypt_renew_hooks:
 - "nginx -t -q && nginx -s reload"
```

* `letsencrypt_renew_email`: `""` - provide an email address to send an email notification of certificate renewal


## TODO:

#### Refactor:
* move all certbot like cron renew to this role and, 

## Author Information
This role:  was created by: Andres bott <contact@andresbott.com>

Documentation generated using: [Ansible-autodoc](https://github.com/AndresBott/ansible-autodoc)

