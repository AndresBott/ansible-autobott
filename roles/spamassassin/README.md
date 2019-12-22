# Ansible Role: spamassassin

Ansible role to install and configure spamassassin as a milter service 

## Tags:

* `role_spamassassin` - Only run this role

## Variables:

* `run_role_spamassassin`: `yes` - flag to disable the role



* `spamassasin_required_score`: `2.5` - 



* `spamassasin_use_bayes`: `1` - enable bayesian filter



* `spamassasin_bayes_auto_learn`: `1` - enable bayesian auto learn



* `spamassasin_scores`: `[]` - disc of rules and weight values, see: http://spamassassin.apache.org/old/tests_3_3_x.html

example: 


```yaml
spamassasin_scores:
  DKIM_SIGNED: 1.0
  DKIM_VALID: -1.5
```

* `spamassasin_whitelist_patterns`: `[]` - use white list patterns like: "friend@somewhere.com", "*@isp.com", or "*.domain.net", make sure that they have valid dkim and spf entries

example: 


```yaml
spamassasin_whitelist_patterns:
  - "*@austrialpin.at"
  - "*@*.example.com"
```

* `spamassasin_bayes_coron`: `{hour:4,minute:0}` - specify when sa learn will run

example: 


```yaml
spamassasin_bayes_cron:
  hour: 4
  minute: 0
```
## TODO:

#### Task:
* add parameter option to disable bayesian learning -  
#### Deprecation:
* remove old spamlearn actions 

## Author Information
This role:  was created by: Andres bott <contact@andresbott.com>

Documentation generated using: [Ansible-autodoc](https://github.com/AndresBott/ansible-autodoc)

