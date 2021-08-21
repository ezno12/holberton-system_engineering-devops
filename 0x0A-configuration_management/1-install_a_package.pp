# installs the lint puppet-lint subcommand
package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem'
}
