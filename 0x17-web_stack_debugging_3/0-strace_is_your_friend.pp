# turn on display_errors in /etc/php5/apach2/php.ini
exec { 'fix typo,  extra p in php extension':
  command => 'sed  -i "s@.phpp@.php@" /var/www/html/wp-settings.php',
  path    => ['/bin','/sbin','usr/bin','usr/sbin']
}
