#  ansible-autobott

This ansible project holds all the resources: playbook, plugins, sample inventory and dependencies (in the form of git submodules) that I use to manage and re-deploy my own servers in a reproducible way.
## About:

Ansible-autbott allows to maintain several services on debian based server with similar offering to a host provider:
* nginx - php based services running as isolated system users
* some additional services like: roundcube, mediawiki, monit or node-red
* email server based on postfix + roundcube

## Getting started
You can see autobott in action on your own using the included vagrant sample.

### Prerequisites
* Vagrant : https://www.vagrantup.com/docs/installation/
* Virtualbox: https://www.virtualbox.org/
  * On MacOS you might want to check: [this article](https://medium.com/@DMeechan/fixing-the-installation-failed-virtualbox-error-on-mac-high-sierra-7c421362b5b5)
* Ansible: https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html
  * On MacOS you can use brew `brew install ansible`
    
### Quick hands on

```bash
git clone https://github.com/AndresBott/ansible-autobott.git
cd ansible-autobott

# start the vagrant vms and perform initial enroll
cd  ansible-autobott/vagrant
vagrant up

# run the complete playbook on the vms
cd ansible-autobott
ansible-playbook autobott.yaml -i vagrant/.vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory

# Optional: run the validations role, if no change is reported all validations have passed.
ansible-playbook autobott.yaml -i vagrant/.vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory -t validation
```

after the playbook finished, you can now login to the sample configured services:
* sample page with https and authentication: [http://private.localhost:9080] user: private password: 1234
* sample php page: [https://php.localhost:9443/]
* sample mediawiki installation: [http://sample-wiki.localhost:9080] user: wiki password: changeme
* monit (keep alive server): [https://monit.localhost:9443]
* gitea server: [http://git.localhost:9080/] user: gitea@gitea.com password: gitea

##  Working with the dev branch 
In order to keep master branch in a stable status, development is only performed and validated on the dev branch
and later pushed to the master branch as a new release.

```bash
cd ansible-autobott
git fetch
git checkout dev
git submodue foreach git checkout dev
```

You can get information about the last run by checking "/root/autobott_info.yaml" on the remote host. 
 
## Extended documentation

For further details check the documentation in the [doc](doc) folder



## Author Information
This playbook  was created by: Andres bott <contact@andresbott.com>


Documentation generated using: [Ansible-autodoc](https://github.com/AndresBott/ansible-autodoc)
