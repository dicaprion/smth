import sqlite3

#Подключение к базе
con = sqlite3.connect("workers.db")

#Создание курсора
c = con.cursor()




#Создание таблиц
c.execute("""
DROP TABLE IF EXISTS Workers
""")
con.commit()

c.execute("""
CREATE TABLE Workers (
   id int auto_increment primary key,
   name varchar(100),
   age int,
   salary int,
   login varchar(100)
)
""")

values = [
   (1, "Дима", 23, 400, "aaa"),
   (2, "Петя", 25, 500, "eee"),
   (3, "Вася", 23, 500, "kkk"),
   (4, "Коля", 30, 1000, "eka"),
   (5, "Иван", 27, 500, "yyy"),
   (6, "Кирилл", 28, 1000, "kak"),
]
#Наполнение таблицы
c.executemany("""INSERT INTO Workers (id, name, age, salary, login) VALUES (?, ?, ?, ?, ?)""", values)




#Подтверждение отправки данных в базу
con.commit()


#
#
# c.execute("""
# select * from Department
#
# """)
#
# print(c.fetchall())
#
c.execute("""
select * from Workers

""")

print(c.fetchall())
#
# #Завершение соединения
c.execute("""
  SELECT * FROM Workers WHERE id IN (3,5,6,10)
""")
con.commit()
print(c.fetchall())

c.execute("""
SELECT * FROM Workers WHERE id IN (3,5,6,10) AND login IN ('eee','zzz', 'ggg')
""")
con.commit()
print(c.fetchall())

c.execute("""
SELECT * FROM Workers WHERE salary >= 500 AND salary <= 1500
""")
con.commit()
print(c.fetchall())

c.execute("""
SELECT id AS workersId, name, age, salary AS workersSalary, login AS workersLogin FROM Workers

""")
con.commit()
print(c.fetchall())

c.execute("""
SELECT MIN(age) FROM Workers
""")
con.commit()
print(c.fetchall())

c.execute("""
SELECT SUM(age) FROM Workers
""")
con.commit()
print(c.fetchall())

c.execute("""
ALTER TABLE Workers
ADD datetime timestamp default NOW
""")
con.commit()

c.execute("""
ALTER TABLE Workers
ADD date timestamp default CURDATE
""")
con.commit()

c.execute("""

""")
con.commit()
c.close()
con.close()
