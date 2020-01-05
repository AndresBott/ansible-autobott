2020/01/05 - Release 1.1.7
* Small corrections
* Remove Minio as it is not used
* Removed submodules dependencies, included all roles into main repo

2019/08/12 - Release 1.1.6
* Small corrections

2019/08/11 - Release 1.1.5
* added samba mounts to role basic host 
* improved spamassasing
* disabled greylist as default

2019/04/21 - Release 1.1.4
* fixed minor issue on dovecot for virtual dirs
* Added postgrey feature to postfix
* fixed minor issue on cron expression for spamassasin 
* Avoid spam-learn concurrent cron execution on multiple accounts

2019/04/21 - Release 1.1.3
* minor fixes on basic_role
* remove shell from vmail user
* spamassasin learn script now invokes a shell
* New validation section: email (send test email, check open ports)

2019/04/21 - Release 1.1.2
* Added role Minio
* Added phpmyadmin to autobott-linux-server-full
* minor typos and fqdn changes

2019/04/06 - 
* spamlearn script now has a feature flag to do a full spam/ham learn the
first time it is executed

2019/03/11  - Release 1.1.1
* Remove variable fqdn and replace by ansible_fqdn
* Add new documentation parts
* Added phpmyadmin recipe

2019/03/10  - Release 1.1.0
* Updated letsencrypt role to use certbot --nginx
* moved letsencrypt cron renew code from webservices role to letsencrypt role
* Improvement in opendkim: report the current public keys in the cli

2019/03/09 - Release 1.0.1
* Roundcube now installs plugins from github
* Minor typos corrected
* Radicale now allows to create users with id and groups with gid
* improve utils/generate_documentation,sh

2019/03/01 - Release 1.0 
* Refactoring complete 
* Published 25 repositories to github

2019/01/10 
* New year, new project! 

I have decided to completely review and refactor my old project ans_webservices,
this time every role is in a different repository, with the goal to make reusable roles
I'm also separating and reducing roles dependencies, the consequence will be some duplicate
configuration values.

I'm mostly copying over the roles and project structure from my old project "ans_webservices", but 
I have decided not to carry over changelog or commits; once the migration has been completed, 
I don't see value on keeping that old code and will discard it. 

* I won't Update every change in the changelog during refactoring. 
