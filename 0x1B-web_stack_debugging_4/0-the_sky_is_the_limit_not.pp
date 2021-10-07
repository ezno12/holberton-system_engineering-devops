# fixes bug where nginx max open files is set to 15. Fix raises it to 4096
exec { 'nginx ulimit increase':
  command => '/bin/sed --in-place "s@ULIMIT=\"-n 15\"@ULIMIT=\"-n 4096\"@" /etc/default/nginx && /etc/init.d/nginx restart',
}
