# -*- coding: utf-8 -*-
import os
import subprocess
import sys

__author__ = 'amplidata'
__tags__   = 'compile',

def main(q, i, params, tags):
    qpackage = params['qpackage']

    targetFolderName = 'pcre-ocaml-release-%s' % (qpackage.version)
    extractedLocation = q.system.fs.joinPaths(q.dirs.tmpDir, targetFolderName)

    # Calculate the required options and environment variables
    additionalPaths = [q.system.fs.joinPaths(q.dirs.baseDir, 'sbin'),
                       q.system.fs.joinPaths(q.dirs.appDir, 'gcc', 'bin'),
                       q.system.fs.joinPaths(q.dirs.appDir, 'gcc', 'sbin')]
    buildEnv = os.environ.copy()
    additionalPaths.append(buildEnv['PATH'])
    buildEnv['PATH'] = os.path.pathsep.join(additionalPaths)
    
    # make 
    args = ['make']
    buildEnv['INCDIRS']=q.system.fs.joinPaths(q.dirs.baseDir,'include','pcre')
    makeProcess = subprocess.Popen(args, stdout=sys.stdout, cwd=extractedLocation, env=buildEnv)
    makeProcess.wait()

    # make htdoc
    args = ['make','htdoc']
    docProcess = subprocess.Popen(args, stdout=sys.stdout, cwd=extractedLocation, env=buildEnv)
    docProcess.wait()

