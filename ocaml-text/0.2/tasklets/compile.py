# -*- coding: utf-8 -*-
import os
import subprocess
import sys

__author__ = 'amplidata'
__tags__   = 'compile',

def main(q, i, params, tags):
    qpackage = params['qpackage']

    targetFolderName = 'text-%s' % (qpackage.version)
    extractedLocation = q.system.fs.joinPaths(q.dirs.tmpDir, targetFolderName)

    # Calculate the required options and environment variables
    additionalPaths = [q.system.fs.joinPaths(q.dirs.baseDir, 'sbin'),
                       q.system.fs.joinPaths(q.dirs.appDir, 'gcc', 'bin'),
                       q.system.fs.joinPaths(q.dirs.appDir, 'gcc', 'sbin')]
    buildEnv = os.environ.copy()
    additionalPaths.append(buildEnv['PATH'])
    buildEnv['PATH'] = os.path.pathsep.join(additionalPaths)
    
    # Build the library
    args = ['make']
    buildProcess = subprocess.Popen(args, stdout=sys.stdout, cwd=extractedLocation, env=buildEnv)
    buildProcess.wait()

    # Make the text.cmxs file
    args = ['ocamlopt', '-shared', '-I', 'src', '-o', 'text.cmxs', 'text.cmxa']
    cmxsProcess = subprocess.Popen(args, stdout=sys.stdout, cwd=q.system.fs.joinPaths(extractedLocation, '_build'), env=buildEnv)
    cmxsProcess.wait()

    # Build the documentation
    args = ['make', 'doc']
    buildDocProcess = subprocess.Popen(args, stdout=sys.stdout, cwd=extractedLocation, env=buildEnv)
    buildDocProcess.wait()

