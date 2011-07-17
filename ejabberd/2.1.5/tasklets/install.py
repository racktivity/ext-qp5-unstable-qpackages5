
__author__ = 'incubaid'
__tags__   = 'install',
import time
def main(q, i, params, tags):
    qpackage = params['qpackage']
    q.platform.ubuntu.install(qpackage.name)
    while not q.system.net.checkListenPort(5222):
        time.sleep(0.5)
    q.platform.ubuntu.stopService(qpackage.name)
    q.platform.ubuntu.disableStartAtBoot(qpackage.name)

