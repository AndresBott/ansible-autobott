# Ansible Role: gitea

Install gitea with the default configuration 

## Tags:

* `role_gitea` - Flag to only run this role

## Variables:

* `run_role_gitea`: `yes` - flag used to disable this role



* `gitea_bind_ip`: `"127.0.0.1"` - ip address to listen to



* `gitea_port`: `"3000"` - port to listen to



* `gitea_db_type`: `"mysql"` - database type: mysql or sqlite3



* `gitea_user`: `gitea` - system user



* `gitea_db_user`: `gitea` - mysql user and database name



* `gitea_db_pass`: `"gitea"` - mysql password



* `gitea_secret_key`: `"random"` - 



* `gitea_domain`: `"localhost"` - domain where gitea is installed, used for generating links



* `gitea_http_port`: `""` - if gitea is setup behind a proxy that is on a non standard port, change this to the termination port, used for url generation



* `gitea_version`: `1.2.2` - current installation version gitea_version: 1.2.2



* `gitea_binary`: `"https://github.com/go-gitea/gitea/releases/download/v{{gitea_version}}/gitea-{{gitea_version}}-linux-amd64"` - current download dir for the current version



* `gitea_sum`: `"2830d77004eb03865fa3860bfb4dd34ccd497070b6f6de667a7de97c3471e07d"` - checksum of the current version gitea_sum: "2830d77004eb03865fa3860bfb4dd34ccd497070b6f6de667a7de97c3471e07d"

example: **upgrade**

 in order to upgrade to a newer gitea version you need to setup all 3 variables accordingly
```yaml
gitea_version: 1.2.3
gitea_binary: "https://github.com/go-gitea/...."
gitea_sum: "2830d77 ... de97c3471e07d"
```

* `gitea_version_delete`: `["1.1.0"]` - dict of older versions that should be deleted


## TODO:

#### Update:
* update gitea binary data 
#### Improvement:
* delete gitea database on deactivation 

## Author Information
This role:  was created by: Andres bott <contact@andresbott.com>

Documentation generated using: [Ansible-autodoc](https://github.com/AndresBott/ansible-autodoc)

