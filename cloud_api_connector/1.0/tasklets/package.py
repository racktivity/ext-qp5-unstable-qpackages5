uthor__ = 'aserver'
__tags__ = 'package',

def main(q, i, params, tags):
    qpackage = params["qpackage"]

    metadataDir = qpackage.getPathMetadata()
    filesDir = q.system.fs.joinPaths(qpackage.getPathFiles())
    if q.system.fs.exists(filesDir):
        q.system.fs.removeDirTree(filesDir)

    q.system.fs.createDir(filesDir)

    q.system.fs.copyDirTree(q.system.fs.joinPaths(q.dirs.varDir, 'src', qpackage.name, 'files'), q.system.fs.joinPaths(filesDir, 'linux'))
    q.system.fs.copyDirTree(q.system.fs.joinPaths(q.dirs.varDir, 'src', qpackage.name, 'tasklets'), q.system.fs.joinPaths(metadataDir, 'tasklets'))
