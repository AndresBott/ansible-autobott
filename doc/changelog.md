

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
