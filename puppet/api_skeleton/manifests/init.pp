# Install and configure the Flask Api Skeleton
class api_skeleton (
    $port = '9010',
    $host = '0.0.0.0',
    $branch_or_revision = 'master',
    $owner = 'vagrant',
    $group = 'vagrant'
) {
  require ::standard_env

  vcsrepo { '/opt/api_skeleton':
    ensure   => latest,
    provider => git,
    source   => 'git://github.com/LandRegistry/charges-api-skeleton',
    revision => $branch_or_revision,
    owner    => $owner,
    group    => $group,
    notify   => Service['api_skeleton'],
  }

  file { '/opt/api_skeleton/bin/run.sh':
    ensure  => 'file',
    mode    => '0755',
    owner   => $owner,
    group   => $group,
    source  => "puppet:///modules/${module_name}/run.sh",
    require => Vcsrepo['/opt/api_skeleton'],
    notify  => Service['api_skeleton'],
  }

  file { '/etc/systemd/system/api_skeleton.service':
    ensure  => 'file',
    mode    => '0755',
    owner   => $owner,
    group   => $group,
    content => template("${module_name}/service.systemd.erb"),
    notify  => [Exec['systemctl-daemon-reload'], Service['api_skeleton']],
  }
  service { 'api_skeleton':
    ensure   => 'running',
    enable   => true,
    provider => 'systemd',
    require  => [
      Vcsrepo['/opt/api_skeleton'],
      File['/opt/api_skeleton/bin/run.sh'],
      File['/etc/systemd/system/api_skeleton.service']
    ],
  }

  file { '/etc/nginx/conf.d/api_skeleton.conf':
    ensure  => 'file',
    mode    => '0755',
    content => template("${module_name}/nginx.conf.erb"),
    owner   => $owner,
    group   => $group,
    notify  => Service['nginx'],
  }

}
