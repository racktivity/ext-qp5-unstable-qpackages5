
__author__ = 'incubaid'
__tags__   = 'install',

def main(q, i, params, tags):
    qpackage = params['qpackage']
    name="postgresql"
    #q.platform.ubuntu.install(qpackage.name)
    q.platform.ubuntu.install(name)
    q.platform.ubuntu.stopService('postgresql')
    q.platform.ubuntu.disableStartAtBoot('postgresql')
    
