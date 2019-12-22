# Ansible Role: parsoid

Install mediawiki parsoid service 

## Tags:

* `role_parsoid` - Flag to only run this roles

## Variables:

* `run_role_parsoid`: `yes` - flag to disable the role



* `parsoid_services`: `[]` - list of different services that will connect to this parsoid instance

example: 


```yaml
parsoid_services:
  - name: wiki1     # used to identify the different wiki installations
    api_uri:        # url to listen to
    namespace:      # the mediawiki namespace (domain)
```

* `parsoid_port`: `8142` - parsoind port



* `parsoid_bind_ip`: `'127.0.0.1'` - parsoind listen ip address



## Author Information
This role:  was created by: Andres bott <contact@andresbott.com>

Documentation generated using: [Ansible-autodoc](https://github.com/AndresBott/ansible-autodoc)

