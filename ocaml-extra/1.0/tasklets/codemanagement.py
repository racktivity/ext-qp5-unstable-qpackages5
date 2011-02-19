
__author__ = 'incubaid'
__tags__   = 'codemanagement',

def main(q, i, params, tags):

    qpackage = params['qpackage']
    
    # inifiles package
    inifilesFileName =  "inifiles-1.2.tar.gz" 
    inifilesRemoteLocation = "http://homepage.mac.com/letaris/%s" % inifilesFileName
    localInifilesArchive = q.system.fs.joinPaths(q.dirs.tmpDir, inifilesFileName)
    q.cloud.system.fs.copyFile(inifilesRemoteLocation, 'file://%s' % localInifilesArchive )
    q.system.fs.targzUncompress(localInifilesArchive , q.system.fs.joinPaths(q.dirs.tmpDir), False)    