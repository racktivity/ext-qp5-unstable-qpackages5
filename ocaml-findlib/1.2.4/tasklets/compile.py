# -*- coding: utf-8 -*-
import os
import subprocess
import sys

__author__ = 'amplidata'
__tags__   = 'compile',

def main(q, i, params, tags):
    qpackage = params['qpackage']

    targetFolderName = 'findlib-%s' % (qpackage.version)
    extractedLocation = q.system.fs.joinPaths(q.dirs.tmpDir, targetFolderName)
    # If yo change the path below, also adapt the PREFIX variable in the Makefile included in the tasklets folder
    localInstallDir = q.system.fs.joinPaths(extractedLocation, 'target-pylabs')

    # First patch the configure script and Makefile to correctly build everything
    configurePatch = q.system.fs.joinPaths(qpackage.getPathMetadata(), 'tasklets', 'configure.patch')
    q.system.process.run('patch configure %s' % configurePatch, showOutput=True, captureOutput=False, cwd=extractedLocation)
    makefilePatch = q.system.fs.joinPaths(qpackage.getPathMetadata(), 'tasklets', 'Makefile.patch')
    q.system.process.run('patch Makefile %s' % makefilePatch, showOutput=True, captureOutput=False, cwd=extractedLocation)

    # Calculate the required options and environment variables
    additionalPaths = [q.system.fs.joinPaths(q.dirs.baseDir, 'sbin'),
                       q.system.fs.joinPaths(q.dirs.appDir, 'gcc', 'bin'),
                       q.system.fs.joinPaths(q.dirs.appDir, 'gcc', 'sbin')]
    buildEnv = os.environ.copy()
    additionalPaths.append(buildEnv['PATH'])
    buildEnv['PATH'] = os.path.pathsep.join(additionalPaths)
    
    options = []

    # Run the configure script with the appropriate options
    args = ['./configure', '-sitelib', q.system.fs.joinPaths(q.dirs.baseDir,'lib','ocaml')]
    args.extend(options)

    # Can't use q.system.process because several environment variables needed to be set on the environment
    configureProcess = subprocess.Popen(args, stdout=sys.stdout, cwd=extractedLocation, env=buildEnv)
    configureProcess.wait()

    # make all
    args = ['make', 'all']
    makeWorldProcess = subprocess.Popen(args, stdout=sys.stdout, cwd=extractedLocation, env=buildEnv)
    makeWorldProcess.wait()

    # make opt
    args = ['make', 'opt']
    makeOptProcess = subprocess.Popen(args, stdout=sys.stdout, cwd=extractedLocation, env=buildEnv)
    makeOptProcess.wait()

    # make install
    args = ['make', 'install', 'prefix=%s' % localInstallDir]
    makeInstallProcess = subprocess.Popen(args, stdout=sys.stdout, cwd=extractedLocation, env=buildEnv)
    makeInstallProcess.wait()

