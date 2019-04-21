

## Useful Ansible parameters
* -l : Limit hosts to group or host
* -t : comma separated list of tags to execute @ see tags
* --list-tasks : list tasks that will be executed
* --check : tries to do a dry-run, does not always work depending on the tasks
* --extra-vars "var=value" : used to pass variables in the cli

for a more complete list check the Ansible documentation

## External inventory

in order to separate code and data, you keep my inventory and host vars in a different repository and then use the -i 
parameter 

    ansible-playbook -i ../path/to/your/inventory 

for example the vagrant inventory:

    ansible-playbook -i vagrant/.vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory
    
## Vault

You can use vault encrypted variables in your project and use a password file to run the playbook.

If you have not specified a password file, use the command line parameter as 

    ansible-vault [encrypt | decrypt] <file> --vault-password-file="/path/to/vault_pass.txt"



# Recepies

## phpmyadmin
    
use `basic_host_extra_apps_host` to install phpmyadmin

    basic_host_extra_apps_host:
    - phpmyadmin

configure a virtual host according to your needs but verify: 
- make sure it has php
- set nginx document_root: "/usr/share/phpmyadmin/"
- change open php open_basedir: ["/usr/share/phpmyadmin/","/usr/share/php"]

    


