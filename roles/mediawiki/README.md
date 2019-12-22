# Ansible Role: mediawiki

Install multiple amount of mediawiki instances 

## Tags:

* `role_mediawiki` - Flag to only run this role

## Variables:

* `run_role_mediawiki`: `yes` - flag used to disable this role



* `mediawiki_instances`: `[]` - list of different mediawiki installations, this allows you to run multiple wikis on one host

example: 


```yaml
mediawiki_instances:
  - name: wiki1                                     # used to identify the different wiki installations
    user: sample_wiki                               # system user to be used
    group: sample_wiki                              # system group to be used
    db_name: sample_wiki                            # database name
    db_user: sample_wiki                            # database user
    db_pass: "changeme"                             # database password
    install_dir: "/wiki/home_dir"                   # root installation dir
    public_html: "/wiki/home_dir/public_html"       # public available directory
    config:
      site_name: "sample wiki"                      # Name of the wiki site
      namespace: "sample_wiki"                      # used to differentiate the wikies in parsoid
      admin_user: "wiki"                            # wiki admin username (defined on installation)
      admin_pass: "changeme"                        # wiki admin password (defined on installation)
      base_url: "https://sample-wiki.localhost"     # full root domain of the wiki
      emergency_contact_mail: info@localhost.com    # emercenty contact email
      password_sender_mail: info@localhost.com      # password reset sender email
      locale: "en_US.utf8"                          # used for imagemagic, needs to be a valid locale
      lang: "en"                                    # Site language code, should be one of the list in ./languages/data/Names.php
      secret_key: "changeme"                        # secret key
      site_upgrade_key: "changeme"                  # used to turn on the web installer while LocalSettings.php is in place
      allowed_extensions:                           # allowed upload extensions
        - pdf
        - tiff
      whitelisted_extensions:                       # whitelist extensions that are normally not allowed
        - txt
        - js
      allow_js: no                                  # allow the upload of javascript files
      enable_visualeditor: yes                      # flag to enable visual editor and usage of parsoid (needed by visual editor)
      visualeditor_parsoid_bind_ip: 127.0.0.1       # parsoid server ip
      visualeditor_parsoid_bind_posrt: 7858         # parsoid server port
      enable_mobile_frontend: yes                   # enable mobile frontend theme
      enable_custom_css: yes                        # add a custom css with small changes (located in templates)
```

* `mediawiki_version`: `1.31.1` - current used versions



* `mediawiki_binary`: `"https://releases.wikimedia.org/mediawiki/1.31/mediawiki-1.31.1.tar.gz"` - current installation source



* `mediawiki_version_delete`: `["1.28.0"]` - installation versions to be deleted



* `mediawiki_VE_version`: `"REL1_31"` - current version of Visual editor to be installed



* `mediawiki_VE_binary`: `"https://extdist.wmflabs.org/dist/extensions/VisualEditor-REL1_31-6854ea0.tar.gz"` - current installation source



* `mediawiki_MFE_version`: `"REL1_31"` - current Mobile Frontend version to be installed



* `mediawiki_MFE_binary`: `"https://extdist.wmflabs.org/dist/extensions/MobileFrontend-REL1_31-7f66849.tar.gz"` - current installation source


## TODO:

#### Validation:
* add a validation to determine if the domain is properly resolved to 127.0.0.1 ( needed for parsoid) 
#### Bug:
* some file permisions are root:root after download + install, ============================================================================================================ Visual Editor / Parsoid ============================================================================================================ 

## Author Information
This role:  was created by: Andres bott <contact@andresbott.com>

Documentation generated using: [Ansible-autodoc](https://github.com/AndresBott/ansible-autodoc)

