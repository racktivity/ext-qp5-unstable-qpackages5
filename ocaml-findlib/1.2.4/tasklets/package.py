# -*- coding: utf-8 -*-
__author__ = 'amplidata'
__tags__ = 'package',

def main(q, i, params, tags):
    qpackage = params["qpackage"]
    
    extractedLocation = q.system.fs.joinPaths(q.dirs.tmpDir, 'findlib-%s' % (qpackage.version))
    localInstallDir = q.system.fs.joinPaths(extractedLocation, 'target-pylabs', 'opt', 'qbase3')

    # Putting the egg in var/tmp. See the install tasklet for part 2
    targetLocation = q.system.fs.joinPaths(qpackage.getPathFiles(), q.platform.name)
    q.system.fs.copyDirTree(localInstallDir, targetLocation, keepsymlinks=True)
