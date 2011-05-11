__author__ = 'aserver'
__tags__   = 'configure',

def main(q, i, params, tags):
    qpackage = params['qpackage']
    configPath = q.system.fs.joinPaths(q.dirs.cfgDir, 'vfs.cfg')
    overWrite = True
    if not q.system.fs.exists(configPath):
        configFile = q.tools.inifile.new(configPath)
    else:
        overWrite = False
    if overWrite:
        configFile = q.tools.inifile.open(configPath)
        configFile.addSection('status')
        configFile.addParam('status', 'mounted', 'False')
        
        configFile.addSection('vfs_paths')
        configFile.addParam('vfs_paths', 'root', '')
        configFile.addParam('vfs_paths', 'metadatapath', '')
        configFile.addParam('vfs_paths', 'localfilestore', '')
        configFile.addParam('vfs_paths', 'mountpoint', '')
    q.extensions.enable('q.system.fuseVFS')
