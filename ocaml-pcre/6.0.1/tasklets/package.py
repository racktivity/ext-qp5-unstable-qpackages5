# -*- coding: utf-8 -*-
__author__ = 'amplidata'
__tags__ = 'package',

def main(q, i, params, tags):
    qpackage = params["qpackage"]
    
    targetFolderName = 'pcre-ocaml-release-%s' % (qpackage.version)
    extractedLocation = q.system.fs.joinPaths(q.dirs.tmpDir, targetFolderName)
    buildLibFolder = q.system.fs.joinPaths(extractedLocation, 'lib')
    buildDocFolder = q.system.fs.joinPaths(buildLibFolder, 'doc','pcre','html')

    # Create the necessary subfolder in the qpackage files section
    platformLocation = q.system.fs.joinPaths(qpackage.getPathFiles(), q.platform.name)
    pcreLibFolder = q.system.fs.joinPaths(platformLocation, 'lib', 'ocaml', 'pcre')
    stubLibsFolder = q.system.fs.joinPaths(platformLocation,'lib', 'ocaml', 'stublibs')
    docFolder = q.system.fs.joinPaths(platformLocation, 'share', 'doc', qpackage.name)

    q.system.fs.createDir(pcreLibFolder)
    q.system.fs.createDir(stubLibsFolder)
    q.system.fs.createDir(docFolder)

    # Copy the library to the correct folder
    q.system.fs.copyFile(q.system.fs.joinPaths(buildLibFolder, 'META'), pcreLibFolder)
    q.system.fs.copyFile(q.system.fs.joinPaths(buildLibFolder, 'libpcre_stubs.a'), pcreLibFolder)
    q.system.fs.copyFile(q.system.fs.joinPaths(buildLibFolder, 'pcre.a'), pcreLibFolder)
    q.system.fs.copyFile(q.system.fs.joinPaths(buildLibFolder, 'pcre.cma'), pcreLibFolder)
    q.system.fs.copyFile(q.system.fs.joinPaths(buildLibFolder, 'pcre.cmi'), pcreLibFolder)
    q.system.fs.copyFile(q.system.fs.joinPaths(buildLibFolder, 'pcre.cmxa'), pcreLibFolder)
    q.system.fs.copyFile(q.system.fs.joinPaths(buildLibFolder, 'pcre.mli'), pcreLibFolder)

    # Copy the native library to the correct folder
    q.system.fs.copyFile(q.system.fs.joinPaths(buildLibFolder, 'dllpcre_stubs.so'), stubLibsFolder)

    # Copy the HTML documentation
    for htmlFile in q.system.fs.listFilesInDir(buildDocFolder):
        q.system.fs.copyFile(htmlFile, docFolder)

