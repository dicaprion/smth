# -*- coding: utf-8 -*-
import thread
import socket
import sqlite3
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def main():
    # создание сокета
    sock = socket.socket()
    # создание сервера
    ip = socket.gethostname()
    port = 55666
    sock.bind((ip, port))
    # список клиентов
    global clientlist
    clientlist = []
    # сообщения
    global mess
    mess = ""
    # отправляю всем клиентам сообщения и записываю в базу данных
    def q():
        # создание базы данных для истории сообщений
        con = sqlite3.connect("history.db")
        c = con.cursor()
        c.execute("""
        DROP TABLE IF EXISTS History
        """)
        con.commit()
        c.execute("""
                   CREATE TABLE History (
                   time TIMESTAMP,
                   user VARCHAR(512),
                   message VARCHAR(4096)
                   )
                   """)


        global mess
        global clientlist
        # заполняю таблицу нашей базы данных
        while True:
            if mess != "":
                cur = mess.split("\n")
                mess = cur.pop()
                for line in cur:
                    print time.strftime("%c") + " " + line
                    user1 = line[:line.find(":")]
                    mes = line[line.find(": "):]
                    values = [(time.strftime("%c"), user1, mes)]
                    c.executemany("""
                    INSERT INTO History (time, user, message) VALUES (?, ?, ?)""", values)
                    con.commit()
                    for client in clientlist:
                        client[0].send(time.strftime("%c") + " " + line)
    #  принимаю сообщения от клиентов
    def w(cli, address,nickname):
        global mess
        while True:
            mess += nickname + ": " + cli.recv(4096) + "\n"
            time.sleep(1)

    thread.start_new_thread(q, ())

    while True:
        # жду одного подключения
        sock.listen(1)
        # получаю данные
        c, adrr = sock.accept()
        #  получаю ник
        nick = c.recv(512)
        time.sleep(0.1)
        #  добавляю нового клиента в список
        clientlist.append((c, nick))
        thread.start_new_thread(w, (c, adrr, nick))

if __name__ == '__main__':
    main()