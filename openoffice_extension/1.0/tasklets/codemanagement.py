
__author__ = 'aserver'
__tags__   = 'codemanagement',

def main(q, i, params, tags):
    qpackage = params['qpackage']
    from pymonkey.clients.hg.HgRecipe import HgRecipe
    recipe = HgRecipe()
    connection = i.hg.connections.findByUrl('http://bitbucket.org/despiegk/doctools')
    recipe.addRepository(connection)

    if q.system.fs.exists( q.system.fs.joinPaths(q.dirs.varDir, 'src', 'lib', 'pymonkey', 'extensions', 'openoffice', 'manage')):
        q.system.fs.removeDirTree(q.system.fs.joinPaths(q.dirs.varDir, 'src', 'lib', 'pymonkey', 'extensions', 'openoffice', 'manage'))

    recipe.addSource(connection, q.system.fs.joinPaths('openoffice_extension', 'manage'), q.system.fs.joinPaths('var', 'src', 'lib', 'pymonkey', 'extensions', 'openoffice', 'manage'))
    recipe.addSource(connection, q.system.fs.joinPaths('openoffice_extension', 'cmdtools'), q.system.fs.joinPaths('var', 'src', 'lib', 'pymonkey', 'extensions', 'openoffice', 'cmdtools'))

    if params['action'] == 'checkout':
        params['action'] = 'export'

    recipe.executeTaskletAction(params['action'])
