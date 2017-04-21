# -*- coding: utf-8 -*-
import socket
import thread
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# функция получения сообщений
def read(sock, msg):
    while True:
        msg = sock.recv(4096)
        print msg

def main():
    sock = socket.socket()
    host = socket.gethostname()
    port = 55666
    nickname = raw_input()
    # попытка подключения к серверу
    try:
        sock.connect((host, port))
    except socket.error:
        print "No such server"
    msg = ""
    # отправка никнейма
    sock.send(nickname)
    # поток на считывание сообщений
    thread.start_new_thread(read, (sock, msg))
    while True:
        text = raw_input()
        sock.send(text)

    sock.close()

if __name__ == '__main__':
    main()