from pexpect import pxssh
import os

class Target:
    def __init__(self, targetIp):
        self.targetIp = targetIp

    def getTargetIp(self):
        return self.targetIp
