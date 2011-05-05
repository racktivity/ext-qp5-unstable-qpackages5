
__author__ = 'aserver'
__tags__   = 'configure',

def main(q, i, params, tags):
    qpackage = params['qpackage']
    cfgPath = q.system.fs.joinPaths(q.dirs.cfgDir, 'vfs.cfg')
    if not q.system.fs.exists(cfgPath):
        cfgFile = q.tools.inifile.new(cfgPath)
    cfgFile = q.tools.inifile.open(cfgPath)
    cfgFile.addSection('vfs_paths')
    localfilestore = q.console.askString('\nPlease enter a path for local file store')
    cfgFile.addParam('vfs_paths', 'localfilestore', localfilestore)
    q.system.fs.createDir(localfilestore)
    metadatapath = q.console.askString('\nPlease enter a path for the metadata')
    cfgFile.addParam('vfs_paths', 'metadatapath', metadatapath) 
    q.system.fs.createDir(metadatapath)
