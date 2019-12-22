# Ansible Role: pybackup

Install pybackup from github 

## Actions:

Actions performed by this role


* run cron based backup jobs that include files and mysql databases 
* use pybackup to fetch the backup files directly to the host you are running ansible from 


## Tags:

* `role_pybackup` - flag to run only this role


* `role_pybackup_remote` - Run the remote backup action, this is only executed if the tag is provided.

## Variables:

* `run_role_pybackup`: `yes` - flag to run this role



* `run_role_pybackup_remote`: `yes` - flag to run the remote backup feature



* `pybackup_jobs`: `[]` - list of backup jobs

example: 


```yaml
pybackup_jobs:
  - name: gitea          # job name
    backup_dir: /vhosts/gitea/home_dir/gitea   # directory that will be backed up
    follow_symlinks: yes # follows sym links when running backup
    output_dir: /vhosts/gitea/backups # directory the backup files will be put, WARNING use only one exclusive directory per job
    tmp_dir: ""          # relative or absolute tmp dir for backup operations, WARN the folder will be deleted on finish
    backup_mysql: gitea  # database name to backup
    keep_old: 4          # amount of older backups to keep
    file_owner: gitea    # change the ownership of the compressed backup file
    file_mode: "0700"    # change the mode of the compressed backup file
    cron:
      enabled: yes
      minute: "0"
      hour: "3"
      day_of_month: "1"
      day_of_week: "*"
      month: "*"
    remote: no           # perform a remote backup of this job when running tag: role_pybackup_remote
```

* `pybackup_remote_tmp`: `/tmp` - tmp location where the files will be copied during remote backup



* `pybackup_remote_fetch_type`: `"ans"` - mechanism used to fetch the file from the remote server, "ans" will use ansible module fetch | "scp" wil use ssh scp



* `pybackup_remote_out`: `"{{ playbook_dir }}/remote_backup"` - local directory where the remote backup will be stored you can pass this variable to the playbook as: --extra-vars "pybackup_remote_out=/home/ans"


## TODO:

#### Improvement:
* improve pybackup and add it to PIP, then install using pip - rename 
#### Verification:
* check if pre-create backup dir is really needed -  

## Author Information
This role:  was created by: Andres bott <contact@andresbott.com>

Documentation generated using: [Ansible-autodoc](https://github.com/AndresBott/ansible-autodoc)

