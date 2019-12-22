# Ansible Role: mysql

Install mysql and perform some basic configurations, inspired in geerlingguy/ansible-role-mysql (MIT)

## Tags:

* `role_mysql` - run only this role

## Variables:

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

## Author Information
This role:  was created by: Andres bott <contact@andresbott.com>

Documentation generated using: [Ansible-autodoc](https://github.com/AndresBott/ansible-autodoc)

