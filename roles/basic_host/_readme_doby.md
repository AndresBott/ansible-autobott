## Use
This role requires root access, the best way it to use a global become: yes

```
- hosts: all
  become: yes
  roles:
    - role: basic_host

```
### Sample configuration

``` 
basic_host_hostname: "ansible-autobott-linux-server-full"

basic_host_extra_host_entires:
  - 127.0.0.1 sample-wiki.localhost

basic_host_ssh_allow_passwd_login: yes

```