# create a manifest that kills a process named killmenow using Puppet

exec { 'pkill':
  command => 'pkill killmenow',
  path    => '/usr/local/bin/:/bin/'
}
