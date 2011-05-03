
__author__ = 'aserver'
__tags__   = 'install',

def main(q, i, params, tags):
    qpackage = params['qpackage']
    #Copy files from the qpackage directory to the sandbox real directory destination
    q.system.fs.copyDirTree(q.system.fs.joinPaths(qpackage.getPathFiles(),'linux64',  'extensions', 'clients', 'googleCalendar'), q.system.fs.joinPaths(q.dirs.baseDir, 'lib', 'pylabs', 'extensions', 'clients', 'googleCalendar'))
    #Add signal for configuration so that the configure tasklet gets executed after qshell is being restarted after installation
    #qpackage.signalConfigurationNeeded()
