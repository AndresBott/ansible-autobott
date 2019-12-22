# Ansible Role: monit

Install monit and perform some basic configurations 

## Tags:

* `role_monit` - Only run the role monit

## Variables:

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
## TODO:

#### Improvement:
* add slack integration https://peteris.rocks/blog/monit-configuration-with-slack/ 

## Author Information
This role:  was created by: Andres bott <contact@andresbott.com>

Documentation generated using: [Ansible-autodoc](https://github.com/AndresBott/ansible-autodoc)

