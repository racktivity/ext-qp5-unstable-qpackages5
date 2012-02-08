
__author__ = 'aserver'
__tags__   = 'install',

def main(q, i, params, tags):
    qpackage = params['qpackage']
    q.platform.ubuntu.install(qpackage.name)

