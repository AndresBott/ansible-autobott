# Ansible Role: opendkim

Install and configure opendkim in ansible-autobott 

## Tags:

* `role_opendkim` - Only run this role


* `role_opendkim_keys` - print current public keys

## Variables:

* `run_role_opendkim`: `yes` - flag to disable the role



* `opendkim_signature_bits`: `1024` - encryption length: [1024 / 2048] this depends on your needs



* `opendkim_socket`: `"unix"` - type of socket: "unix" for unix socket | "inet" for http



* `opendkim_port`: `54321` - port used when using inet



* `opendkim_socket_location`: `"/var/spool/postfix/opendkim/opendkim.sock"` - location of the socket if type unix, autobott postfix expects this location.



## Author Information
This role:  was created by: Andres bott <contact@andresbott.com>

Documentation generated using: [Ansible-autodoc](https://github.com/AndresBott/ansible-autodoc)

