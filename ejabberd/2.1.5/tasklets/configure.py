
__author__ = 'aserver'
__tags__   = 'configure',

def main(q, i, params, tags):
    qpackage = params['qpackage']
    q.platform.ubuntu.stopService(qpackage.name)
    q.platform.ubuntu.disableStartAtBoot(qpackage.name)
