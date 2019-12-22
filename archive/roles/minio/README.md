# Ansible Role: minio

Install minio and perform some basic configurations 

## Tags:

* `role_minio` - 

## Variables:

* `run_role_minio`: `yes` - Flag to disable the role



* `minio_disable`: `no` - disable and uninstall minio, data will be left



* `minio_uid`: `no` - define a uid for the user



* `minio_group`: `minio` - system group



* `minio_gid`: `no` - define a gid for the group



* `minio_bind_ip`: `"127.0.0.1"` - ip address to listen to



* `minio_port`: `9000` - minio port



* `minio_install_client`: `yes` - Install the minio client app



* `minio_current_version`: `2019-03-13` - see minio_sources for available versions or provide your own



* `minio_client_current_version`: `2019-03-13` - see minio_client_sources for available versions or provide your own



## Author Information
This role:  was created by: Andres bott <contact@andresbott.com>

Documentation generated using: [Ansible-autodoc](https://github.com/AndresBott/ansible-autodoc)

