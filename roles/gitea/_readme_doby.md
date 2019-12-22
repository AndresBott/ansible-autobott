## Use:
This role requires root access, the best way it to use a global become: yes
```
- hosts: git
  become: yes
  roles:
    - role: gitea
```
### Sample configuration:
``` 
run_role_gitea: yes
gitea_dir: "/home_dir/gitea/install"
gitea_data_dir: "/home_dir/gitea/data"
gitea_domain: git.localhost

```

After the first installation you can login with user: 'gitea@gitea.com' password: 'gitea'
