# Report

### About
you can most probably obtain all this information during development using `absible-autodoc -p < annotation >`,
you can also use "all" instead of a specific annotation.

## Duplicated tags:

This is useful to identify duplicated tags in different roles that might be conflicting.

* `validation_http` in files:

        roles/validation/tasks/main.yaml (line: 81) 
        roles/validation/tasks/main.yaml (line: 96) 

* `role_dovecot` in files:

        roles/dovecot/tasks/main.yaml (line: 6) 
        roles/email-service/tasks/main.yaml 


## Duplicated variables:

This is useful to identify duplicated variables in different roles that might be conflicting.


Documentation generated using: [Ansible-autodoc](https://github.com/AndresBott/ansible-autodoc)