# Ansible Role: node-red

Install node-red 

## Tags:

* `role_nodered` - Flag to only run this roles

## Variables:

* `run_role_nodered`: `yes` - flag to disable the role



* `nodered_user`: `nodered` - system user



* `nodered_uid`: `no` - define a uid for the user



* `nodered_group`: `nodered` - system group



* `nodered_gid`: `no` - define a gid for the group



* `nodered_dir`: `/opt/nodered` - installation dir



* `nodered_service_name`: `nodered` - systemd service name



* `nodered_port`: `9663` - port to start node-red



* `nodered_pacakges`: `[node-red,node-red-dashboard]` - node-red packages (not needed to change)



## Author Information
This role:  was created by: Andres bott <contact@andresbott.com>

Documentation generated using: [Ansible-autodoc](https://github.com/AndresBott/ansible-autodoc)

