# Script to automate the task of creating a custom HTTP header response, but with Puppet.
exec { 'http header':
  command  => 'sudo apt-get update -y;
	sudo apt-get install nginx -y;
	sudo sed -i "s/server_name _;/server_name _;\n\n\tadd_header X-Served-By $HOSTNAME;\n/" /etc/nginx/sites-enabled/default;
	sudo service nginx restart',
  provider => shell,
}
