#!/bin/sh
wget -O /tmp http://apt.puppetlabs.com/puppetlabs-release-precise.deb
dpkg -i /tmp/puppetlabs-release-precise.deb
apt-get -y install puppet
rm -r /etc/puppet
git clone git://github.com/pocams/wp-puppet.git /etc/puppet
puppet apply --modulepath=/etc/puppet/modules /etc/puppet/manifests/site.pp