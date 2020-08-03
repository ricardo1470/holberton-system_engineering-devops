# kill process named killmenow
$paths = ['/usr/bin']

exec { 'killmenow':
  path    => $paths,
  command => 'pkill -f killmenow',
}
