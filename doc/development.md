

## Using report
If you want to add a custom message to the end of the playbook, 
add a debug tastk with name if the task name starts with `[REPORT]`

```$xslt
- name: "[REPORT]Test Report message"
  debug:
    msg: " this is a custom message"
```

