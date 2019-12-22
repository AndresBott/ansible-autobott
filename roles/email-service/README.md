# Ansible Role: email-service

Maintain ansible-autobott email accounts 

## Actions:

Actions performed by this role


* email mysql - create the shared mysql database to be used by dovecot and postfix 
* SSL/TLS - create a certificate for the email server (self signed or let's encrypt) 
* setup email accounts (domains, addresses and alias) 


## Tags:

* `email_service` - Only run this role


* `email_accounts` - only update email accounts, if there has been any change


* `role_dovecot` - 

## Variables:

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



* `email_server_domain`: `"mail.{{ ansible_fqdn }}"` - email server main domain, the server can handle multiple domain email addresses but needs one primary domain for the clients to connect to. the



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

## Author Information
This role:  was created by: Andres bott <contact@andresbott.com>

Documentation generated using: [Ansible-autodoc](https://github.com/AndresBott/ansible-autodoc)

