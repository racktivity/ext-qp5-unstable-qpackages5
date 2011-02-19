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

    def replword(file, listrepl):
            data = open(file, "rb").read()
            for origword,replacement in listrepl :
                    newdata = re.sub(origword, replacement, data)
                    f = open(file, "wb")
                    f.write(newdata)
                    f.close()
    
    
  
    ejabberdAppDir = q.system.fs.joinPaths(q.dirs.appDir, 'ejabberd')
    if 'agent' in q.config.list() and 'main' in q.config.getConfig('agent'):
        hostname = q.config.getConfig('agent')['main']['xmppserver']
    else:
        hostname = q.gui.dialog.askString('\nPlease enter the FQDN',defaultValue='dmachine.office.aserver.com')
    q.system.fs.changeDir(q.system.fs.joinPaths(ejabberdAppDir, 'etc', 'ejabberd'))
    replword('ejabberd.cfg', [('FQDNHERE',hostname)] )
    q.system.process.execute('/opt/qbase3/bin/openssl req -config /opt/qbase3/apps/ejabberd/etc/ejabberd/openssl.cnf -batch -newkey rsa:1024 -keyout ejabberd.pem -nodes -x509 -days 3650 -out ejabberd.cer')
    pemfile = open('ejabberd.pem', "rb").read()
    cerfile = open('ejabberd.cer', "rb").read()
    f = open('ejabberd.pem', "a")
    f.write('\n')
    f.write(cerfile)
    f.close()
    #qbaseinfo=pwd.getpwnam('qbase')
    #os.chown('ejabberd.pem', qbaseinfo.pw_uid , qbaseinfo.pw_gid)
    q.system.unix.chown(ejabberdAppDir, 'qbase', 'qbase', True)
    os.chmod('ejabberd.pem', 0400)
