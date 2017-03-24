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
ADD dt datetime default '2017-03-24 08:48:54'
""")
con.commit()
print(c.fetchall())

c.execute("""
ALTER TABLE Workers
ADD dt2 date default '2017-03-24'
""")
con.commit()
print(c.fetchall())

c.execute("""
SELECT * FROM Workers
""")

c.execute("""
SELECT strftime('%Y', dt), strftime('%m', dt), strftime('%d',dt) FROM Workers
""")
con.commit()
print(c.fetchall())

c.execute("""
UPDATE Workers SET dt='2017-03-24 08:48:32' WHERE id=3
""")
con.commit()
c.execute("""
SELECT strftime('%M', dt), strftime('%S', dt) FROM Workers
""")
con.commit()

c.execute("""
SELECT * FROM Workers WHERE strftime('%M',dt) > strftime('%S',dt)
""")
con.commit()
print(c.fetchall())

c.close()
con.close()
