
__author__ = 'aserver'
__tags__ = 'package',

def main(q, i, params, tags):
    qpackage = params["qpackage"]
    q.system.fs.removeDirTree(qpackage.getPathFiles())
    
