# Install and configure the Flask Conveyancer API
class conveyancer_api (
    $port = '9015',
    $host = '0.0.0.0',
    $branch_or_revision = 'master'
) {
  require ::standard_env

  vcsrepo { '/opt/conveyancer_api':
    ensure   => latest,
    provider => git,
    source   => 'git://github.com/LandRegistry/charges-conveyancer-api',
    revision => $branch_or_revision,
    owner    => 'vagrant',
    group    => 'vagrant',
    notify  => Service['conveyancer_api'],
  }

  file { '/opt/conveyancer_api/bin/run.sh':
    ensure  => 'file',
    mode    => '0755',
    owner   => 'vagrant',
    group   => 'vagrant',
    source  => "puppet:///modules/${module_name}/run.sh",
    require => Vcsrepo['/opt/conveyancer_api'],
    notify  => Service['conveyancer_api'],
  }

  file { '/etc/systemd/system/conveyancer_api.service':
    ensure  => 'file',
    mode    => '0755',
    owner   => 'vagrant',
    group   => 'vagrant',
    content => template("${module_name}/service.systemd.erb"),
    notify  => [Exec['systemctl-daemon-reload'], Service['conveyancer_api']],
  }
  service { 'conveyancer_api':
    ensure   => 'running',
    enable   => true,
    provider => 'systemd',
    require  => [
      Vcsrepo['/opt/conveyancer_api'],
      File['/opt/conveyancer_api/bin/run.sh'],
      File['/etc/systemd/system/conveyancer_api.service']
    ],
  }

  file { '/etc/nginx/conf.d/conveyancer_api.conf':
    ensure  => 'file',
    mode    => '0755',
    content => template("${module_name}/nginx.conf.erb"),
    owner   => 'vagrant',
    group   => 'vagrant',
    notify  => Service['nginx'],
  }

}
