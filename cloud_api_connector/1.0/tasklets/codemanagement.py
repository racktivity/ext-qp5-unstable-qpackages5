__author__ = 'aserver'
__tags__     = "codemanagement",
__priority__ = 1

def match(q, i, params, tags):
    return True

def main(q, i, params, tags):
    qpackage = params['qpackage']

    from pymonkey.clients.hg.HgRecipe import HgRecipe
    branch = ['default']

    recipe = HgRecipe()
    repository = ['https://bitbucket.org/aserver/cloud_api_connector']

    connection = i.hg.connections.findByUrl(repository[0])
    taskletsexportDir = q.system.fs.joinPaths(q.dirs.varDir, 'src', qpackage.name, 'tasklets')
    filesexportDir = q.system.fs.joinPaths(q.dirs.varDir, 'src', qpackage.name, 'files')

    if q.system.fs.exists(taskletsexportDir):
        q.system.fs.removeDirTree(taskletsexportDir)
    if q.system.fs.exists(filesexportDir):
        q.system.fs.removeDirTree(filesexportDir)

    recipe.addRepository(connection)
    recipe.addSource(connection, q.system.fs.joinPaths('api'), q.system.fs.joinPaths(filesexportDir, 'lib', 'pylabs', 'extensions', 'api'),branch=branch[0])
    recipe.addSource(connection, q.system.fs.joinPaths('cloud_api_clients'), q.system.fs.joinPaths(filesexportDir, 'lib', 'pylabs', 'extensions', 'cloud_api_clients'),branch=branch[0])
    recipe.addSource(connection, q.system.fs.joinPaths('osis'), q.system.fs.joinPaths(filesexportDir, 'libexec', 'osis'),branch=branch[0])
    recipe.addSource(connection, q.system.fs.joinPaths('qpackage', qpackage.name), q.system.fs.joinPaths(taskletsexportDir),branch=branch[0])

    recipe.executeTaskletAction(params["action"])

