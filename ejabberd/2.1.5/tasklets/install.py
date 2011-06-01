
__author__ = 'incubaid'
__tags__   = 'install',
import time
def main(q, i, params, tags):
    qpackage = params['qpackage']
    q.platform.ubuntu.install(qpackage.name)
    time.sleep(2)
    q.platform.ubuntu.stopService(qpackage.name)
    q.platform.ubuntu.disableStartAtBoot(qpackage.name)

