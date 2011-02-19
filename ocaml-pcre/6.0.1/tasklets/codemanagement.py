# -*- coding: utf-8 -*-
__author__ = 'amplidata'
__tags__   = 'codemanagement',

def main(q, i, params, tags):
    qpackage = params['qpackage']
    
    # Download the ounit sources
    downloadSource = 'http://hg.ocaml.info/release/pcre-ocaml/archive/'

    # QPackage version number should match the upstream version
    targetFolder = '%s-%s' % (qpackage.name, qpackage.version)
    fileName = 'release-%s.tar.gz' % (qpackage.version)

    remoteArchive = q.system.fs.joinPaths(downloadSource, fileName)
    localArchive = 'file://%s' % q.system.fs.joinPaths(q.dirs.tmpDir, fileName)
    q.cloud.system.fs.copyFile(remoteArchive, localArchive)
    q.system.fs.targzUncompress(q.system.fs.joinPaths(q.dirs.tmpDir, fileName), q.system.fs.joinPaths(q.dirs.tmpDir), False)
