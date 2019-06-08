import os
from socket import *

class TryHardHelpers:
    # Checks if the target is up
    def isTargetAlive(self, targetIp):
        # Sends only one Ping packet to the Target
        targetStatus = os.system("ping -c 1 " + targetIp)

        if targetStatus == 0:
            return True

        return False

    # Scans for ports to see if SSH, FTP, and SMB are open for exploit
    def isPortOpen(self, targetIp, targetPort):
        socketOp = socket(AF_INET, SOCK_STREAM)
        result = socketOp.connect_ex((targetIp, targetPort))

        if result == 0:
            print('[*] Port ' + targetPort +'is open. \n')
            return True

        print('[*] Port ' + targetPort + 'is closed. \n')
        return False


    
