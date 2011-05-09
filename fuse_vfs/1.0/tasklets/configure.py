
__author__ = 'aserver'
__tags__   = 'configure',

def main(q, i, params, tags):
    qpackage = params['qpackage']
    configPath = q.system.fs.joinPaths(q.dirs.cfgDir, 'vfs.cfg')

    if not q.system.fs.exists(configPath):
        configFile = q.tools.iniFile.new(configPath)
    else:
        overWrite = q.console.askYesNo('Overwrite existing configuration?')
    if overWrite:
        configFile.addSection('status')
        configFile.addParam('status', 'mounted', 'False')
        
        configFile.addSection('vfs_paths')
        configFile.addParam('vfs_paths', 'root', q.console.askString('Please enter a default location for the root of the virtual file system'))
        configFile.addParam('vfs_paths', 'metadatapath', q.console.askString('Please enter a default location for the metadata of the virtual file system'))
        configFile.addParam('vfs_paths', 'localfilestore', q.console.askString('Please enter a default location for large files'))
        configFile.addParam('vfs_paths', 'mountpoint', q.console.askString('Please enter a default location for the mountpoint of the virtual file system'))
    q.extensions.enable('q.system.fuseVFS')
