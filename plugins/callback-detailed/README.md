# ansible-callback-detailed
Ansible callback plugin that  produces very detailed yet accessible output.

# About

This callback plugin extends the default one adding detailed information about every action performed by every
module, if the module details to return have been configured in this plugin.

For example the user module will print the username currently being modified.

Additionally, the end of the playbook run the changed actions will be reported again, 
you can also add individual messages to be added to the report.

# doc
### Add messages to the repord:

Create a debug task where the name starts with `[REPORT]`, example:

```$xslt
- name: [REPORT] this will be printed in the final report
  debug:
    msg: "this is the message to print, you can also use variables like this: {{ ansible_host }}"
``` 

### Debug
If you want to get some debug information while making changes on the plugin, set the debug property to True
