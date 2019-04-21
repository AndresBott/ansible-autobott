

# Using extrernal inventories

You can run ansible with an external invetory: 

    ansible-playbook -i ../path/to/inventory

## Example
when working with autobott you should use an external inventory, use a similar structure to the provided vagrant one
as a starting point to define your own needs:

    my_server/
    my_server/group_vars/
    my_server/group_vars/all.yaml     
    my_server/group_vars/linux-servers.yaml
    my_server/group_vars/mail-servers.yaml
    my_server/group_vars/nginx-web-servers.yaml
    
    my_server/host_vars/
    my_server/host_vars/my_server1.com.yaml
    my_server/host_vars/my_server2.com.yaml
    
    my_server/production.yaml
    
production.yaml example:

    all:
      children:
    
        #============================================================================================================
        # linux server groups based on server role
        #============================================================================================================
        nginx-web-servers:
          hosts:
            my_server1.com
            my_server2.com
    
        mail-servers:
          hosts:
            my_server1.com
            my_server2.com
            

NOTE: group vars with the prefix "vag-" are used in the sample to avoid conflicts wiht the external inventroy

## About

I run a small set of non homogeneous server, therefore my main configuration is done per-host, and this is also 
reflected in the sample vagrant configuration file, as it resembles the most my production environment. 