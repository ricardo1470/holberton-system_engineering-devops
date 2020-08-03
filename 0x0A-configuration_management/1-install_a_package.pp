# install package pupped
# exec resource executes an apt-get update command.
# package resource installs the package puppet-lint, 
# defining that the apt-get update resource is a requirement,
exec { 'apt-get update':
  command   => '/usr/bin/apt-get update'
}

package {'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}
