# Puppet Script to fix Nginx: 24: Too Many Open Files Error 
exec { 'fixNginx':
  command => 'sed -i "s/-n 15/-n 4096/" /etc/default/nginx && sudo service nginx restart',
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}