# This manifest fixes a 500 error on Apache WP servers
exec { 'phpfix':
  command => "sed -ie 's/locale.phpp/locale.php/' /var/www/html/wp-settings.php",
  path    => '/bin'
}
