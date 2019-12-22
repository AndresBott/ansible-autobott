# Ansible Role: roundcube

Install n amount of roundcube instances 

## Tags:

* `role_roundcube` - Flag to only run this role

## Variables:

* `run_role_roundcube`: `yes` - flag used to disable this role



* `roundcube_instances`: `[]` - list of roundcube instances that will be installed

example: 


```yaml
roundcube_instances:
  - name: webmail                                 # used to identify the different roundcube installations
    user: roundcube                               # system user to be used
    group: roundcube                              # system group to be used
    db_name: roundcube                            # database name
    db_user: roundcube                            # database user
    db_pass: "changeme"                           # database password
    install_dir: "{{webservices_root}}/roundcube/home_dir" # root installation dir
    public_html: "{{webservices_root}}/roundcube/home_dir/public_html" # public available directory
    tmp_dir: "{{webservices_root}}/roundcube/home_dir/tmp"
    config:
      ignore_certificate_validation: yes           # this is needed for simple self signed certificates, and should no be used in production
      mail_server: "mail.localhost"
      cypher: "Quaba75eesdahfoh2eizay8i"           # exactly 24 chars
      plugins: []                                  # see <installdir>/plugins, these are provided with roundcube
      github_plugins: []         # select from predefined plugins to be installed from github, see variable roundcube_github_plugins
```

* `roundcube_current_version`: `1.3.3` - roundcube version to install



* `roundcube_sources`: `` - roundcube installation candidates, this can be changed per configuration

example: 


```yaml
roundcube_sources:
  1.3.3:
    url: https://github.com/roundcube/roundcubemail/releases/download/1.3.3/roundcubemail-1.3.3-complete.tar.gz
    sum: "05d9856c966c0d93accabf724e7ff2fd493bba1a57c44247ed0a2aacd617c879"
```

* `roundcube_manual_plugins`: `<see examples >` - list of manual installable plugins, this can be extended per configuration.

example: 


```yaml
roundcube_github_plugins:
    - name: carddav
      url: https://github.com/blind-coder/rcmcarddav/releases/download/v3.0.2/carddav-3.0.2.zip
      repo_name: carddav
      plugin_file: carddav.php
      config_file: carddav.config-inc.php.j2
```
## TODO:

#### Update:
* update roundcube to latest version 

## Author Information
This role:  was created by: Andres bott <contact@andresbott.com>

Documentation generated using: [Ansible-autodoc](https://github.com/AndresBott/ansible-autodoc)

