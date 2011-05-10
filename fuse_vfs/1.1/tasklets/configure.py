
__author__ = 'aserver'
__tags__   = 'configure',

def main(q, i, params, tags):
    qpackage = params['qpackage']
    configPath = q.system.fs.joinPaths(q.dirs.cfgDir, 'vfs.cfg')
    overWrite = True
    if not q.system.fs.exists(configPath):
        configFile = q.tools.inifile.new(configPath)
    else:
        overWrite = q.console.askYesNo('\nOverwrite existing configuration?')
    if overWrite:
        configFile = q.tools.inifile.open(configPath)
        configFile.addSection('status')
        configFile.addParam('status', 'mounted', 'False')
        
        configFile.addSection('vfs_paths')
        configFile.addParam('vfs_paths', 'root', q.console.askString('\nPlease enter a default location for the root of the virtual file system'))
        configFile.addParam('vfs_paths', 'metadatapath', q.console.askString('Please enter a default location for the metadata of the virtual file system'))
        configFile.addParam('vfs_paths', 'localfilestore', q.console.askString('Please enter a default location for large files'))
        configFile.addParam('vfs_paths', 'mountpoint', q.console.askString('Please enter a default location for the mountpoint of the virtual file system'))
    q.extensions.enable('q.system.fuseVFS')
