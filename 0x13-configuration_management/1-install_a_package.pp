# This manifest installs the latest version of puppet-lint
package { 'puppet-lint':
ensure   => 'latest',
provider => 'gem',
}
