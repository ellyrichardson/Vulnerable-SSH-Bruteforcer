import sys
sys.path.append("../ssh_operations")
sys.path.append("../../helpers")

from helpers.helpers import TryHardHelpers
from ssh_operations.ssh_operations import SSHOperations

class MainOperations:
    def checkOperations(self, targetList, user, targetPasswords):
        cmd = TryHardHelpers()
        sshOps = SSHOperations()

        portList = [21,22,445]

        # Checks open ports
        for target in targetList:
            if cmd.isTargetAlive(target) == True:
                print('[+] ' + target + ' is up.')

                for port in portList:
                    if cmd.isPortOpen(target, port):
                        print('[*] Port ' + port +'is open. \n')
                        sshOps.parseCredentialsForTarget(target, user, \
                            targetPasswords)

                    else:
                        print('[*] Port ' + port +'is closed. \n')
            else:
                print('[-] ' + target + ' is not up')


    #def checkOperations(targetIp, )


