import sys
sys.path.append("./helpers")
sys.path.append("./operations")

import argparse

from helpers.helpers import TryHardHelpers
from operations.main_operations.main_operations import MainOperations

def main():
    parser = argparse.ArgumentParser('usage%prog ' + \
        '-H <target hosts> -u <user> -F <password list>')

    parser.add_argument('-H', dest='tgtHosts',\
        help='specify target hosts', type=argparse.FileType('r'))
    parser.add_argument('-u', dest='user',\
        help='specify the user')
    parser.add_argument('-F', dest='passwdFile',\
        help='specify password file', type=argparse.FileType('r'))

    (options, args) = parser.parse_args()

    hosts = options.tgtHosts
    passwdFile = options.passwdFile
    user = options.user

    if hosts == None or passwdFile == None or user == None:
        print(parser.usage)
        exit(0)

    mainOps = MainOperations()
    mainOps.checkOperations(hosts, user, passwdFile)

if __name__ == '__main__':
    main()
    

    