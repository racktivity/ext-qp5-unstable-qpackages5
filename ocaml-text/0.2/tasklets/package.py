# -*- coding: utf-8 -*-
__author__ = 'amplidata'
__tags__ = 'package',

def main(q, i, params, tags):
    qpackage = params["qpackage"]
    
    targetFolderName = 'text-%s' % (qpackage.version)
    extractedLocation = q.system.fs.joinPaths(q.dirs.tmpDir, targetFolderName)
    buildLibFolder = q.system.fs.joinPaths(extractedLocation, '_build')
    buildDocFolder = q.system.fs.joinPaths(buildLibFolder, 'text.docdir')

    # Create the necessary subfolder in the qpackage files section
    platformLocation = q.system.fs.joinPaths(qpackage.getPathFiles(), q.platform.name)
    textLibFolder = q.system.fs.joinPaths(platformLocation, 'lib', 'ocaml', 'text')
    stubLibsFolder = q.system.fs.joinPaths(platformLocation,'lib', 'ocaml', 'stublibs')
    docFolder = q.system.fs.joinPaths(platformLocation, 'share', 'doc', qpackage.name)

    q.system.fs.createDir(textLibFolder)
    q.system.fs.createDir(stubLibsFolder)
    q.system.fs.createDir(docFolder)

    # Copy the library to the correct folder
    q.system.fs.copyFile(q.system.fs.joinPaths(buildLibFolder,'src','encoding.cmi'), textLibFolder)
    q.system.fs.copyFile(q.system.fs.joinPaths(buildLibFolder,'src','encoding.cmx'), textLibFolder)
    q.system.fs.copyFile(q.system.fs.joinPaths(buildLibFolder,'src','encoding.mli'), textLibFolder)
    q.system.fs.copyFile(q.system.fs.joinPaths(buildLibFolder,'META'), textLibFolder)
    q.system.fs.copyFile(q.system.fs.joinPaths(buildLibFolder,'src','libtext_stubs.a'), textLibFolder)
    q.system.fs.copyFile(q.system.fs.joinPaths(buildLibFolder,'text.a'), textLibFolder)
    q.system.fs.copyFile(q.system.fs.joinPaths(buildLibFolder,'text.cma'), textLibFolder)
    q.system.fs.copyFile(q.system.fs.joinPaths(buildLibFolder,'src','text.cmi'), textLibFolder)
    q.system.fs.copyFile(q.system.fs.joinPaths(buildLibFolder,'src','text.cmx'), textLibFolder)
    q.system.fs.copyFile(q.system.fs.joinPaths(buildLibFolder,'text.cmxa'), textLibFolder)
    q.system.fs.copyFile(q.system.fs.joinPaths(buildLibFolder,'text.cmxs'), textLibFolder)
    q.system.fs.copyFile(q.system.fs.joinPaths(buildLibFolder,'src','text.mli'), textLibFolder)

    # Copy the native library to the correct folder
    q.system.fs.copyFile(q.system.fs.joinPaths(buildLibFolder,'src','dlltext_stubs.so'), stubLibsFolder)

    # Copy the HTML documentation
    for htmlFile in q.system.fs.listFilesInDir(buildDocFolder):
        q.system.fs.copyFile(htmlFile, docFolder)

