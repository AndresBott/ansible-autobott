# Ansible Role: basic_host

Basic reusable role for debian based hosts, this role will take care of some basic housekeeping.

## Actions:

Actions performed by this role


#### Enroll:
* Create a system user "ans" and allow password less sudo to that user. 
* Manage ssh keys for the system user "ans", this are the ones allowed to make changes on the ansible managed systems. 
#### Install and upgrade:
* Configure debian sources.list and sources.list.d 
* install some set of basic needed apps 
* upgrade the system 
#### Hostname:
* change the hostname 
* update /etc/hosts 
#### Cron:
* update cron MAILTO 
#### Locale:
* generate and configure the locales of the system 
#### Users:
* create and delete users 
#### Smb-client:
* install samba (cifs) client and configure mounting points 

## Tags:

* `enroll` - run the the initial enrollment actions of the system


* `role_basic_host` - only run the role basichost


* `configuration` - run configuration tasks


* `upgrade` - perform a system upgrade


* `action_upgrade` - perform a system upgrade, same as upgrade


* `users` - update user definitions and credentials


* `facts` - 


* `samba` - 

## Variables:

* `basic_host_user`: `ans` - username for ansible login user



* `basic_host_uid`: `900` - uid for ansible login user



* `basic_host_group`: `ans` - group for ansible login user



* `basic_host_gid`: `900` - gid for ansible login user



* `basic_host_home`: `/home/ans` - home dir for ansible login user



* `basic_host_root_bashrc`: `true` - create a custom .brashrc for root user



* `basic_host_ssh_keys`: `[]` - User keys allowed to login as ansible admin, thus run ansible playbook



* `basic_host_ssh_keys_revoked`: `[]` - User keys that are no longer allowed to login as ansible admin



* `basic_host_sources_distro_country`: `ch` - select the country prefix for the distro template



* `basic_host_sources_d`: `[]` - additional sources to be added to /etc/apt/sources.list.d



* `basic_host_cache_valid_time`: `3600` - change the valid cache time of apt when running ansible multiple times



* `basic_host_installed_apps`: `[apt,ca-certificates]` - list of apps to be installed,



* `basic_host_extra_apps`: `[]` - second list of apps that can be defined



* `basic_host_extra_apps_host`: `[]` - third list of apps that can be defined at host level



* `basic_host_hostname`: `""` - define the host's hostname



* `basic_host_fqdn`: `"{{ ansible_fqdn }}"` - define the host's Fully qualified domain name



* `basic_host_extra_host_entires`: `[]` - add extra entries to /etc/hosts



* `basic_host_cron_notification_mail`: `""` - enable cron to send emails to that address



* `basic_host_locale_to_be_generated`: `["en_US.UTF-8 UTF-8","es_ES.UTF-8 UTF-8"]` - list of locales to be generated (take care to use value from /usr/share/i18n/SUPPORTED,as locale-gen exit with code 0 even with errors...)



* `basic_host_locale_lang`: `en_US.UTF-8` - 



* `basic_host_locale_all`: `""` - 



* `basic_host_locale_language`: `""` - 



* `basic_host_locale_numeric`: `""` - 



* `basic_host_locale_time`: `""` - 



* `basic_host_locale_monetary`: `""` - 



* `basic_host_locale_paper`: `""` - 



* `basic_host_locale_identification`: `""` - 



* `basic_host_locale_name`: `""` - 



* `basic_host_locale_address`: `""` - 



* `basic_host_locale_telephone`: `""` - 



* `basic_host_locale_measurement`: `""` - 



* `basic_host_ssh_allow_passwd_login`: `no` - allow users to ssh using password



* `basic_host_ssh_allow_passwd_login_group`: `""` - if basic_host_ssh_allow_passwd_login is set to no, you can limit password ssh to certain group, set to empty string to disable



* `basic_host_ssh_sftp`: `yes` - enable sftp using openssh, see groups definitions to configure sftp jails



* `basic_host_ssh_X11forwarding`: `no` - enable X11 forwarding, this should not be needed on a normal server



* `basic_host_create_group_for_every_user`: `true` - Create a group for every user and make that their primary group



* `basic_host_users_group`: `users` - If we're not creating a per-user group, then this is the group all users belong to



* `basic_host_users_default_shell`: `/bin/bash` - default shell for created users



* `basic_host_users_create_homedirs`: `true` - Create home dirs for created users



* `basic_host_groups`: `[]` - List of groups to create

example: 


```yaml
basic_host_groups:
  - name: sftp
    gid: 402
    sftp_jail:
      enabled:  yes
      base_dir: "/home" #jail home dir: i.e /home/%u or /vhosts/%u
      allow_password: yes
      umask: "0077"
```

* `basic_host_system_users`: `[]` - List of system users to be created

example: 


```yaml
basic_host_system_users:
  - username: "tardis"
    name: "that blue box"
    groups: [ 'trenzalore','gallifrey']
    uid: 2001
    gid: 2001
```

* `basic_host_users`: `[]` - List of users to be added

example: 


```yaml
basic_host_users:
  - username: jdoe
    name: "The Doctor"
    groups: ['sudo', 'trenzalore','gallifrey']  # empty string removes user from all secondary groups
    uid: 2001
    gid: 2001 # optional
    password: "{{ secred_my_user_passwd | password_hash('sha512', 65534 | random(seed=inventory_hostname) | string) }}" # encrypted
    ssh_key:
      - "ssh-rsa AAAAA.... john@laptop"
      - "ssh-rsa AAAAB.... doctor@desktop"
    ssh_key_revoked: []
    shell: /bin/bash # optional
    home:  #commentout for default
    create_home: true
    home_is_sftp_jail: false
    bashrc: true #optional
```

* `basic_host_users_extra`: `[]` - second list of users to be added, this allows to define users at different locations



* `basic_host_users_deleted`: `[]` - list of users + user groups to NOT to be present. WARNING this will not delete their home



* `basic_host_smb`: `no` - set to yes to install smb client, tools and configure mounting points



* `basic_host_smb_mounts`: `no` - set to yes to install smb client, tools and configure mounting points

example: 


```yaml
basic_host_smb_mounts:
  - name: data1
    host: //SERVER/Data
    mount: /home/user/mount
    user: user
    group: group
    pass: pass
    mount_options: ""
```
## TODO:

#### Improvement:
* add automatic system update with cron 

## Author Information
This role:  was created by: Andres bott <contact@andresbott.com>

Documentation generated using: [Ansible-autodoc](https://github.com/AndresBott/ansible-autodoc)

