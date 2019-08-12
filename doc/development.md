

## Using report
If you want to add a custom message to the end of the playbook, 
add a debug tastk with name if the task name starts with `[REPORT]`

```$xslt
- name: "[REPORT]Test Report message"
  debug:
    msg: " this is a custom message"
```

# Git

## Change branches 

````bash
git submodule foreach git fetch

# change branch
git submodule foreach git checkout [master|dev] 

# merge squash
git submodule foreach git merge [master|dev] --squash

# commit the squashed changes
git submodule foreach git commit -m "merge branch dev for release xxx" 

```` 