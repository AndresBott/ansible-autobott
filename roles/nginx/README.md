# Ansible Role: nginx

Install nginx and perform some basic configurations 

## Tags:

* `role_nginx` - Only run the role nginx

## Variables:

* `nginx_pgks_to_install`: `[nginx,nginx-full]` - packages to be installed



* `nginx_user`: `www-data` - groupname for web services, this is default debian, don't change



* `nginx_worker_processes`: `2` - should be same as cpu count for best performance



* `nginx_worker_connections`: `1024` - max ammount of concurrent connections per worker



* `nginx_client_max_body_size`: `30m` - max size of a request body, i.e file upload + form data



* `nginx_default_error_page`: `""` - define path to a error page



* `nginx_modules`: `[]` - list of modules to be enabled

example: 


```yaml
nginx_modules:
  - mod-http-auth-pam.conf
  - mod-http-dav-ext.conf
  - mod-http-echo.conf
  - mod-http-geoip.conf
  - mod-http-image-filter.conf
  - mod-http-subs-filter.conf
  - mod-http-upstream-fair.conf
  - mod-http-xslt-filter.conf
  - mod-mail.conf
  - mod-stream.conf
```

## Author Information
This role:  was created by: Andres bott <contact@andresbott.com>

Documentation generated using: [Ansible-autodoc](https://github.com/AndresBott/ansible-autodoc)

