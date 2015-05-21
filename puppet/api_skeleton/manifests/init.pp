# Install and configure the Flask Api Skeleton
class api_skeleton (
    $port = '9000',
    $host = '0.0.0.0',
    $branch_or_revision = 'master'
) {
  require ::standard_env

  vcsrepo { '/opt/api-skeleton':
    ensure   => latest,
    provider => git,
    source   => 'git://github.com/LandRegistry/charges-api-skeleton',
    revision => $branch_or_revision,
    owner    => 'vagrant',
    group    => 'vagrant',
  }

}
