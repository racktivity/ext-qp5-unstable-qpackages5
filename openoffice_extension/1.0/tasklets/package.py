
__author__ = 'aserver'
__tags__ = 'package',

def main(q, i, params, tags):
    qpackage = params["qpackage"]
    filesDir = q.system.fs.joinPaths(qpackage.getPathFiles())
    q.system.fs.removeDirTree(filesDir)
    q.system.fs.createDir(filesDir)

    for relativePath in (q.system.fs.joinPaths('lib', 'pymonkey', 'extensions', 'openoffice', 'manage'), q.system.fs.joinPaths('lib', 'pymonkey', 'extensions', 'openoffice', 'cmdtools')):
        q.system.fs.copyDirTree(q.system.fs.joinPaths(q.dirs.varDir, 'src', relativePath), q.system.fs.joinPaths(filesDir, 'linux', relativePath))
        q.system.fs.createEmptyFile(q.system.fs.joinPaths(qpackage.getPathFiles(), 'linux', relativePath, '..', '__init__.py'))    
