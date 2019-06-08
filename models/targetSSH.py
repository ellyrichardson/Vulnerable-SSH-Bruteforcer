from pexpect import pxssh
from .target import Target

class SSHTarget(Target):
    def __init__(self, targetIp, targetUname, targetPword):
        super(SSHTarget, self).__init__(targetIp)

        self.targetUname = targetUname
        self.targetPword = targetPword
        #self.session = self.connectToTarget()


        ###### Only leave the getters in this cmd, and then declare the target
        ##### cmds from other class so SSHTarget can be a data model!

    def getTargetUname(self):
        return self.targetUname

    def getTargetPword(self):
        return self.targetPword
