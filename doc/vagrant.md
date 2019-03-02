# Vagrant
THis contains limited information about vagrant relevant for this project, check the vagrant documentation for full details 

## About the VMs:

The vagrant file defines 3 VMS: 
* ansible-autobott-linux-server-full : a host that is intended to represent the complete functionality of the
playbook.
* ansible-autobott-linux-server-mini: a very minimalistic host indented to verify that the default values are sufficient.
* ansible-autobott-linux-server-email: a email server only host, to verify that settings from web server and email 
server are not dependent.



## Commands
restart the provisioning
```$xslt
# start the vms
vagrant up

# restart + provision
vagrant reload --provision

# vagrant only provison
vagrant provision

# stop the vms
vagrant halt
```


## Managing vms
```bash
# view base images
vagrant box list

# delete a VM
vagrant destroy

# delete a box
vagrant box remove [--box-version]

```

        
## Ansible on vagrant inventory
run ansible playbook againts vagrant inventory
```bash
ansible-playbook [-l vagrant] [-t basichost]  autobott.yaml -i vagrant/.vagrant/povisioners/ansible/inventory/vagrant_ansible_inventory

```

r 