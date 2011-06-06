
__author__ = 'aserver'
__tags__   = 'codemanagement',

def main(q, i, params, tags):
    from clients.mercurial.HgRecipe import HgRecipe
    recipe = HgRecipe()
    #Create a connection to the bitbucket repo
    connection = i.config.clients.mercurial.findByUrl('https://bitbucket.org/incubaid/pylabs-core')
    #Add the repo to the recipe
    recipe.addRepository(connection)

    qpackage = params['qpackage']
    #Define an export directory in tmp dir to clone the repo in
    exportdir = q.system.fs.joinPaths(q.dirs.tmpDir, qpackage.name, qpackage.version)
    #Make sure the export dir is empty before cloning
    q.system.fs.removeDirTree(exportdir)
    
    #Add source to the recipe with the directory from hg repo code you want to put with the full path you need this code to be copied to in the sandbox
    recipe.addSource(connection, 'extensionsadditional/pylabs_diff', q.system.fs.joinPaths(exportdir, 'extensions', 'pylabs_diff'))
    recipe.executeTaskletAction(params['action'])
