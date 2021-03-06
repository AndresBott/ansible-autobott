# Ansible Role: php-fpm

Install php-fom and perform some basic configurations 

## Actions:

Actions performed by this role


#### Install:
* Install and configure php-fpm 
* make sure that logrotate is enabled for /var/log/php/*.log 
#### Uninstall:
* uninstall php-fpm if run_role_php_fpm is set to no / false 

## Tags:

* `role_php_fpm` - run only php-fpm role

## Variables:

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


## TODO:

#### Verify:
* make sure that the php worker logs are being rotated, maybe need to create a group and add the workers to the group 

## Author Information
This role:  was created by: Andres bott <contact@andresbott.com>

Documentation generated using: [Ansible-autodoc](https://github.com/AndresBott/ansible-autodoc)

