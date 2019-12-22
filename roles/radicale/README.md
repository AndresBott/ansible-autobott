# Ansible Role: radicale

Install radicale v2 

## Actions:

Actions performed by this role


* Install Radicale2 in a Venv using PIP 
* setup regular git commits for radicale collections 


## Tags:

* `role_radicale` - Flag to only run this roles

## Variables:

* `run_role_radicale`: `yes` - flag to disable the role



* `radicale_user`: `radicale` - service user



* `radicale_uid`: `no` - service uid, set to no to use system automatic



* `radicale_group`: `radicale` - service main group



* `radicale_gid`: `no` - service main gid, set to no to use system automatic



* `radicale_install_dir`: `/opt/radicale` - main installation location



* `radicale_data_dir`: `/opt/radicale/data` - data location



* `radicale_bound_ip`: `127.0.0.1` - service listen ip address



* `radicale_port`: `5232` - service port



## Author Information
This role:  was created by: Andres bott <contact@andresbott.com>

Documentation generated using: [Ansible-autodoc](https://github.com/AndresBott/ansible-autodoc)

