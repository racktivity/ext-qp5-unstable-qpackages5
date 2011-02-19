
__author__ = 'aserver'
__tags__ = 'package',

def main(q, i, params, tags):
    qpackage = params["qpackage"]
    
    targetLocation = q.system.fs.joinPaths(qpackage.getPathFiles(), q.platform.name)
    
    ocamlLibDir = q.system.fs.joinPaths( targetLocation, 'lib' , 'ocaml' )
    
    ocamlFilePatterns = [ 
        "*.mli" , 
        "*.cmo" , 
        "*.cma" ,
        "*.cmi" ,
        "*.cmx" ,
        "*.cmxa" ,
        "*.a" ,
        "META" ]

    # inifiles package
    inifilesBuildDir = q.system.fs.joinPaths(q.dirs.tmpDir, "inifiles-1.2")
    inifilesDestination = q.system.fs.joinPaths( ocamlLibDir, "inifiles" )
    
    if not q.system.fs.isDir ( inifilesDestination ) :
        q.system.fs.createDir( inifilesDestination )
    if not q.system.fs.isDir ( inifilesDestination ) :
        q.eventhandler.raiseCriticalError( "Could not create directory %s aborting" % inifilesDestination ) 
    for pattern in ocamlFilePatterns :
        for file in q.system.fs.listFilesInDir( inifilesBuildDir, filter=pattern) :
            q.system.fs.copyFile( file, inifilesDestination )
            