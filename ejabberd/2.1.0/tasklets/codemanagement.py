
__author__ = 'aserver'
__tags__   = 'configure',

def main(q, i, params, tags):
    #Use this to checkout from mercurial
    #from pymonkey.clients.hg.HgRecipe import HgRecipe
    #recipe = HgRecipe()
    
    # Or just extract the files from the bundle
    qpackage = params['qpackage']
    if qpackage.download(suppressErrors=True):
        qpackage.extract()  # extract the bundle
    else:
        pass # we dont have a bundle yet
