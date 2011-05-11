
__author__ = 'aserver'
__tags__   = 'install',

def main(q, i, params, tags):
    qpackage = params['qpackage']
    #Copy files from the qpackage directory to the sandbox real directory destination
    q.system.fs.copyDirTree(q.system.fs.joinPaths(qpackage.getPathFiles(),'linux64',  'extensions', 'fuse_vfs'), q.system.fs.joinPaths(q.dirs.baseDir, 'lib', 'pylabs', 'extensions', 'fuse_vfs'))
    qpackage.signalConfigurationNeeded() 
