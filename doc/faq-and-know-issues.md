
# FAQ

* does this work with other linux distributions that are not debian?

At the moment, this only works with debian stable, but adapting the roles to other distros, should not be complicated;
pull requests are welcome.


# Troubleshoot

### ansible_fqdn
Autobott uses the variable `ansible_fqdn` to define the servers name on several places. 

This variable  contains the value of the remote server IPs rDNS request and if it is not found it will fallback to 
your hosts definition. If this does not fit your needs, you might overwrite this variable on a per host basis. 

### opendkim

In order to get opendkim mails signed correctly, you need to publish your public key as an TXT record for your
domain, you can see the keys running the tag: `role_opendkim_keys`

### letsencrypt

In order to correctly issue certificates, the domain you are requesting the certificate for needs to be under your
control, to prove this, you need to point the domain or subdomian to the server you are running letsencrypt.




# Known issues

