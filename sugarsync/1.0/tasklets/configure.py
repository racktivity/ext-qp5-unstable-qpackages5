
__author__ = 'aserver'
__tags__   = 'configure',

def main(q, i, params, tags):
    qpackage = params['qpackage']
    q.extensions.enable('q.clients.sugarsync') 
    q.extensions.enable('q.clients.sugarsyncapi')

