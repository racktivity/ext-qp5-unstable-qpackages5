
__author__ = 'aserver'
__tags__   = 'install',

def main(q, i, params, tags):
    qpackage = params['qpackage']
    file_name = 'swift-install-script.sh'
    file_path = q.system.fs.joinPaths(q.dirs.tmpDir, file_name)
    swift_install_script = """
#!/bin/bash

set -e
if ! test x`whoami` == 'xroot'; then
    echo 'This script should run as root!'
    exit 1
fi

die () {
        echo "Error:"
        echo $@
        echo
        exit 1
}

my_aptitude () {
        echo "Running aptitude " $@
        aptitude $@ || die "Aptitude failed"
}

echo
echo 'Installing dependency packages...'
# Update preparing for python-software-properties
my_aptitude update
my_aptitude -y install python-software-properties
add-apt-repository ppa:swift-core/release || die "Adding APT repository failed"
# Another update to include the newly added Swift Core Release repository
my_aptitude update
my_aptitude -y install curl memcached python-configobj python-setuptools python-simplejson python-xattr sqlite3 python-webob python-eventlet python-greenlet python-pastedeploy python-netifaces
echo

echo
echo 'Creating swift user and directories...'
adduser --system --home /srv/swift --group --disabled-login swift || die "Failed to create swift user"
mkdir /srv/swift/storage
chown swift /srv/swift/storage

mkdir -p /etc/swift/object-server /etc/swift/container-server /etc/swift/account-server /var/run/swift || die "Failed creating folders"
chown -R swift:swift /var/run/swift
echo

echo
echo 'Installing packages...'
my_aptitude -y install swift swift-account swift-container swift-object swift-proxy
echo

echo
echo 'Creating configuration files...'
cat > /etc/swift/proxy-server.conf << EOF
[DEFAULT]
bind_port = 8080
user = swift
log_facility = LOG_LOCAL1

[pipeline:main]
pipeline = healthcheck swift3 cache tempauth proxy-server

[app:proxy-server]
use = egg:swift#proxy
allow_account_management = true

[filter:tempauth]
use = egg:swift#tempauth
user_admin_admin = admin .admin .reseller_admin
user_test_tester = testing .admin
user_test2_tester2 = testing2 .admin
user_test_tester3 = testing3

[filter:healthcheck]
use = egg:swift#healthcheck

[filter:cache]
use = egg:swift#memcache

[filter:swift3]
use = egg:swift#swift3
EOF

SUFFIX=$(dd if=/dev/urandom count=512 bs=1 2>/dev/null | sha512sum | awk '{ print $1 }')
cat > /etc/swift/swift.conf << EOF
[swift-hash]
swift_hash_path_suffix = ${SUFFIX}
EOF

cat > /etc/swift/account-server/1.conf << EOF
[DEFAULT]
devices = /srv/swift
mount_check = false
bind_port = 6012
user = swift
log_facility = LOG_LOCAL2

[pipeline:main]
pipeline = account-server

[app:account-server]
use = egg:swift#account

[account-replicator]

[account-auditor]

[account-reaper]
EOF

cat > /etc/swift/container-server/1.conf << EOF
[DEFAULT]
devices = /srv/swift
mount_check = false
bind_port = 6011
user = swift
log_facility = LOG_LOCAL2

[pipeline:main]
pipeline = container-server

[app:container-server]
use = egg:swift#container

[container-replicator]

[container-updater]

[container-auditor]
EOF

cat > /etc/swift/object-server/1.conf << EOF
[DEFAULT]
devices = /srv/swift
mount_check = false
bind_port = 6010
user = swift
log_facility = LOG_LOCAL2

[pipeline:main]
pipeline = object-server

[app:object-server]
use = egg:swift#object

[object-replicator]

[object-updater]

[object-auditor]
EOF
echo

echo
echo 'Setting up system...'
cat > /usr/local/sbin/swift-remakerings << EOF
#!/bin/bash

cd /etc/swift
rm -f *.builder *.ring.gz backups/*.builder backups/*.ring.gz

swift-ring-builder object.builder create 18 1 1
swift-ring-builder object.builder add z1-127.0.0.1:6010/storage 1
swift-ring-builder object.builder rebalance

swift-ring-builder container.builder create 18 1 1
swift-ring-builder container.builder add z1-127.0.0.1:6011/storage 1
swift-ring-builder container.builder rebalance

swift-ring-builder account.builder create 18 1 1
swift-ring-builder account.builder add z1-127.0.0.1:6012/storage 1
swift-ring-builder account.builder rebalance
EOF
chmod a+x /usr/local/sbin/swift-remakerings

swift-remakerings || die "Failure while building rings"

swift-init all start || die "Failed to launch Swift services"

"""
    q.system.fs.remove(file_path, onlyIfExists=True)
    q.system.fs.writeFile(file_path, swift_install_script)
    q.system.unix.chmod(q.dirs.tmpDir, 0774, filePattern=file_name)
    q.action.start('Installing %s %s' % (qppackage.name, qpackage.version))
    exit_code, stdout, stderr = q.system.process.run(file_path, showOutput=True, captureOutput=False, stopOnError=False, user='root')
    if exit_code == 0:
        q.system.fs.remove(file_path, onlyIfExists=True)
        q.action.stop(failed=False)
    elif exit_code != 0:
        q.log.logger('Failed to install %s %s') % (qpackage.name, qpackage.version)
        q.qction.stop(failed=True)
    elif exit_code == -1:
        q.log.logger('Installation of %s %s was killed') % (qpackage.name, qpackage.version)
        q.qction.stop(failed=True)
    else:
        q.log.logger('Unknown error occured while installing %s %s') % (qpackage.name, qpackage.version)
        q.action.stop(failed=True)

