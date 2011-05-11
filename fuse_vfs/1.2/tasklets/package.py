
__author__ = 'aserver'
__tags__ = 'package',

def main(q, i, params, tags):
    qpackage = params["qpackage"]
    exportdir = q.system.fs.joinPaths(q.dirs.tmpDir, qpackage.name, qpackage.version)
    #Copy files from the tmp export dir to the qpackages dir
    q.system.fs.copyDirTree(exportdir, q.system.fs.joinPaths(qpackage.getPathFiles(), 'linux64'))

