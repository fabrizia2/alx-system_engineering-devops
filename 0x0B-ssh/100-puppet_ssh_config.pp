#Configuration to add lines in ssh config
exec { 'Append Line IdentityFile':
  command => '/bin/echo -e "IdentityFile ~/.ssh/school\nPasswordAuthentication no" >> /etc/ssh/ssh_config',
  path    => '/etc/ssh/ssh_config',
}
