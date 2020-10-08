#  fix our stack so that we get to 0
# and remember that when something is going wrong.
file { 'replace last line':
     ensure  => present,
     path    => '/etc/default/nginx'
     content => 'ULIMIT="-n 4096"',
	    }

service { 'nginx':
	ensure    => running,
	subscribe => File['/etc/default/nginx']
}
