
__author__ = 'aserver'
__tags__   = 'install',

def main(q, i, params, tags):
    qpackage = params['qpackage']
    #Copy files from the qpackage directory to the sandbox real directory destination
    q.system.fs.copyDirTree(q.system.fs.joinPaths(qpackage.getPathFiles(),'linux64',  'extensions', 'clients', 'sugarsync'), q.system.fs.joinPaths(q.dirs.baseDir, 'lib', 'pylabs', 'extensions', 'clients', 'sugarsync'))
    #Add signal for configuration so that the configure tasklet gets executed after qshell is being restarted after installation
    #qpackage.signalConfigurationNeeded() 
