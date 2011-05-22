
__author__ = 'aserver'
__tags__   = 'install',

def main(q, i, params, tags):
    qpackage = params['qpackage']
    #Copy files from the qpackage directory to the sandbox real directory destination
    q.system.fs.copyDirTree(q.system.fs.joinPaths(qpackage.getPathFiles(),'generic',  'extensions', 'pylabs_vfs'), q.system.fs.joinPaths(q.dirs.baseDir, 'lib', 'pylabs', 'extensions', 'pylabs_vfs'))
    #Add signal for configuration so that the configure tasklet gets executed after qshell is being restarted after installation
    #qpackage.signalConfigurationNeeded()
    #enabling the package
    #q.extensions.enable('q.system.vfs')
