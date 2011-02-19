# -*- coding: utf-8 -*-
__author__ = 'amplidata'
__tags__   = 'codemanagement',

def main(q, i, params, tags):
    qpackage = params['qpackage']
    
    # Download the ounit sources
    downloadSource = 'http://forge.ocamlcore.org/frs/download.php/211/'

    # QPackage version number should match the upstream version
    targetFolder = 'text-%s' % (qpackage.version)
    fileName = '%s.tar.gz' % targetFolder

    remoteArchive = q.system.fs.joinPaths(downloadSource, fileName)
    localArchive = 'file://%s' % q.system.fs.joinPaths(q.dirs.tmpDir, fileName)
    q.cloud.system.fs.copyFile(remoteArchive, localArchive)
    q.system.fs.targzUncompress(q.system.fs.joinPaths(q.dirs.tmpDir, fileName), q.system.fs.joinPaths(q.dirs.tmpDir), False)
