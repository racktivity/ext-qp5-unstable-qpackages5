__author__   = "aserver"
__tags__     = "configure",
__priority__ = 1

import os,os.path,re,pwd
#from socket import gethostname;

def match(q, i, params, tags):
    return True

def main(q, i, params, tags):
    # Copy the files for this platform from the files/ folder to sandbox
    qpackage = params['qpackage']

    ########## Move to qconfig for ejabberd! 
    ejabberdAppDir = q.system.fs.joinPaths(q.dirs.appDir, 'ejabberd')
    if 'agent' in q.config.list() and 'main' in q.config.getConfig('agent'):
        hostname = q.config.getConfig('agent')['main']['hostname']
    else:
        hostname = q.gui.dialog.askString('\nPlease enter the FQDN',defaultValue='dmachine.sso.daas.com')

    ########################## 


    q.system.fs.changeDir(q.system.fs.joinPaths(ejabberdAppDir, 'etc', 'ejabberd'))
    q.system.process.execute('/opt/qbase3/bin/openssl req -config %s/ejabberd/etc/ejabberd/openssl.cnf -batch -newkey rsa:1024 -keyout ejabberd.pem -nodes -x509 -days 3650 -out ejabberd.cer'%q.dirs.appDir)
    pemfile = open('ejabberd.pem', "rb").read()
    cerfile = open('ejabberd.cer', "rb").read()
    f = open('ejabberd.pem', "a")
    f.write('\n')
    f.write(cerfile)
    f.close()
    q.system.unix.chown(ejabberdAppDir, 'qbase', 'qbase', True)
    os.chmod('ejabberd.pem', 0400)

    q.manage.ejabberd.init()

    q.manage.ejabberd.startChanges()

    q.manage.ejabberd.cmdb.nodeName = hostname

    if hostname not in q.manage.ejabberd.cmdb.hosts:
        q.manage.ejabberd.cmdb.addHost(hostname)

    q.manage.ejabberd.cmdb.ejabberdUser = i.config.qbase.users.getConfig()['local_daemon_user']
    
    if not i.config.qbase.users.getConfig()['app_root_user'] in q.manage.ejabberd.cmdb.users:
        q.manage.ejabberd.cmdb.addUser(i.config.qbase.users.getConfig()['app_root_user'], hostname, i.config.qbase.users.getConfig()['app_root_passwd'])
        q.manage.ejabberd.cmdb.addACL('admin', ['user', i.config.qbase.users.getConfig()['app_root_user'], hostname])

    q.manage.ejabberd.cmdb.save()
    q.manage.ejabberd.applyConfig()
