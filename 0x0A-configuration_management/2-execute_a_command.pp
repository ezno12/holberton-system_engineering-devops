# kills the 'killmenow' process
service { 'killmenow':
  ensure => stopped,
  enable => false
}
