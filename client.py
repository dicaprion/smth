# -*- coding: utf-8 -*-
import socket
import thread
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
def readchat(sock, msg):
    while True:
        msg = sock.recv(4096)
        print msg


def main():
    sock = socket.socket()
    host = socket.gethostname()
    port = 55666
    nickname = raw_input()
    try:
        sock.connect((host, port))

    except socket.error:
        print "No such server"
    msg = ""
    sock.send(nickname)
    thread.start_new_thread(readchat, (sock, msg))
    while True:
        text = raw_input()
        sock.send(text)

    sock.close()

if __name__ == '__main__':
    main()