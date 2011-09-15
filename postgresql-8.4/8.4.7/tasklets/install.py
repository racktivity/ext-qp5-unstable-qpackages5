
__author__ = 'incubaid'
__tags__   = 'install',

def main(q, i, params, tags):
    name="postgresql"
    qpackage = params['qpackage']
    q.platform.ubuntu.install(name)
    q.platform.ubuntu.stopService('postgresql')
    q.platform.ubuntu.disableStartAtBoot('postgresql')
    
