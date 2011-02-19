# -*- coding: utf-8 -*-
import os
import subprocess
import sys

__author__ = 'incubaid'
__tags__   = 'compile',

def main(q, i, params, tags):
    qpackage = params['qpackage']
    
    additionalPaths = [q.system.fs.joinPaths(q.dirs.baseDir, 'sbin'),
                       q.system.fs.joinPaths(q.dirs.appDir, 'gcc', 'bin'),
                       q.system.fs.joinPaths(q.dirs.appDir, 'gcc', 'sbin')]
    buildEnv = os.environ.copy()
    additionalPaths.append(buildEnv['PATH'])
    buildEnv['PATH'] = os.path.pathsep.join(additionalPaths)

    #inifiles package
    inifilesBuildDir = q.system.fs.joinPaths(q.dirs.tmpDir, "inifiles-1.2")
    ## make reallyall
    args = ['make', 'reallyall']
    makeWorldProcess = subprocess.Popen(args, stdout=sys.stdout, cwd=inifilesBuildDir, env=buildEnv)
    makeWorldProcess.wait()

