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
   login varchar(100),
   description varchar(100),
   dt datetime,
   dt2 date,
   dt3 time
)
""")

values = [
   (1, "Дима", 23, 400, "aaa", "jkfkdhk  h hh  gf f fffgjgdhfdf ggfgf" ),
   (2, "Петя", 25, 500, "eee", "dkjfdhfdjk h g g gg ggg kjdfdkfjdkf"),
   (3, "Вася", 23, 500, "kkk", " lkffjkdjfkdjfkdf fff ffffffff"),
   (4, "Коля", 30, 1000, "eka", "soskkd jfjdkfgejweb  nn nnfdd"),
   (5, "Иван", 27, 500, "yyy", "kjdkjj hh kkkkk [[[ jdkesd hf"),
   (6, "Кирилл", 28, 1000, "kak", "sjjjj j jjjrrrrr dlsdksldksl lkfdfdf"),
]
#Наполнение таблицы
c.executemany("""INSERT INTO Workers (id, name, age, salary, login, description) VALUES (?, ?, ?, ?, ?, ?)""", values)




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
#
# # задание 1
# c.execute("""
#   SELECT * FROM Workers WHERE id IN (3,5,6,10)
# """)
# con.commit()
# print(c.fetchall())
#
# # задание 2
# c.execute("""
#
# SELECT * FROM Workers WHERE id IN (3,5,6,10) AND login IN ('eee','zzz', 'ggg')
# """)
# con.commit()
# print(c.fetchall())
# # задание 3
# c.execute("""
# SELECT * FROM Workers WHERE salary >= 500 AND salary <= 1500
# """)
# con.commit()
# print(c.fetchall())
#
# # задание 4
# c.execute("""
# SELECT id AS workersId, name, age, salary AS workersSalary, login AS workersLogin FROM Workers
#
# """)
# con.commit()
# print(c.fetchall())
#
# # задание 5
# c.execute("""
# SELECT MIN(age) FROM Workers
# """)
# con.commit()
# print(c.fetchall())
#
# # задание 6
# c.execute("""
# SELECT SUM(age) FROM Workers
# """)
# con.commit()
# print(c.fetchall())
#
# # задание 7
# c.execute("""
# ALTER TABLE Workers
# ADD dt datetime
# """)
# con.commit()
#
# # задание 8
# c.execute("""
# ALTER TABLE Workers
# ADD dt2 date
# """)
# con.commit()
#
# c.execute("""INSERT INTO Workers(dt) SELECT datetime('now')
# """)
# con.commit()
#
# c.execute("""INSERT INTO Workers(dt2) SELECT date('now')
# """)
# con.commit()
#
#
# c.execute("""
# UPDATE workers SET dt = (SELECT datetime('now'))
# """)
#
# c.execute("""
# UPDATE workers SET dt2 = (SELECT date('now'))
# """)
#
# c.execute("""
# SELECT * FROM Workers
# """)
# con.commit()
# print(c.fetchall())
#
# # задание 9
# c.execute("""
# SELECT strftime('%Y', dt), strftime('%m', dt), strftime('%d',dt) FROM Workers
# """)
# con.commit()
# print(c.fetchall())
#
# # задание 10
# c.execute("""
# SELECT * FROM Workers WHERE strftime('%M',dt) > strftime('%S',dt)
# """)
# con.commit()
# print(c.fetchall())
#
# #

# 1
c.execute("""
SELECT * FROM Workers WHERE id IN (1,2,3,5,14)
""")
con.commit()
print(c.fetchall())


# 2
c.execute("""
SELECT * FROM Workers WHERE login IN ('eee','bbb', 'zzz')
""")
con.commit()
print(c.fetchall())

# 3
c.execute("""
SELECT * FROM Workers WHERE id IN (1,2,3,7,9) AND login IN ('user','admin', 'Ivan') AND salary > 300
""")
con.commit()
print(c.fetchall())
# 4
c.execute("""
SELECT Salary FROM Workers WHERE Salary BETWEEN 100 AND 1000
""")
con.commit()
print(c.fetchall())
# 5
c.execute("""
SELECT * FROM Workers WHERE (id BETWEEN 3 AND 10) AND Salary BETWEEN 300 AND 500
""")
con.commit()
print(c.fetchall())
# 6
c.execute("""
SELECT id AS userId, name, age, salary AS userSalary, login AS userLogin FROM Workers
""")
con.commit()

# 7
c.execute("""
SELECT DISTINCT Salary FROM Workers
""")
con.commit()
print(c.fetchall())

# 8
c.execute("""
SELECT DISTINCT age FROM Workers
""")
con.commit()
print(c.fetchall())

# 9
c.execute("""
SELECT MIN(salary) FROM Workers
""")
con.commit()
print(c.fetchall())

# 10
c.execute("""
SELECT MAX(salary) FROM Workers
""")
con.commit()
print(c.fetchall())

# 11
c.execute("""
SELECT SUM(salary) FROM Workers
""")
con.commit()
print(c.fetchall())

# 12
c.execute("""
SELECT SUM(salary)FROM Workers WHERE age BETWEEN 21 AND 25
""")
con.commit()
print(c.fetchall())

# 13
c.execute("""
SELECT SUM(salary) FROM Workers WHERE id IN(1,2,3,5)
""")
con.commit()
print(c.fetchall())

# 14
c.execute("""
SELECT AVG(Salary) FROM Workers
""")
con.commit()
print(c.fetchall())

# 15
c.execute("""
SELECT AVG(age) FROM Workers
""")
con.commit()
print(c.fetchall())

# 16
c.execute("""SELECT * FROM Workers WHERE dt2 > (SELECT DATE('now'))
""")
con.commit()
print(c.fetchall())

# 17
c.execute("""INSERT INTO Workers(dt) SELECT DATETIME('now')
""")
con.commit()
print(c.fetchall())

# 18
c.execute("""INSERT INTO Workers(dt2) SELECT DATE('now')
""")
con.commit()
print(c.fetchall())

# 19
c.execute("""INSERT INTO Workers(dt3) SELECT TIME('now')
""")
con.commit()
print(c.fetchall())

# 20
c.execute("""SELECT * FROM workers WHERE strftime('%Y', dt2) = 2016
""")
con.commit()
print(c.fetchall())

# 21
c.execute("""SELECT * FROM workers WHERE strftime('%m', dt2) = 3
""")
con.commit()
print(c.fetchall())

# 22
c.execute("""SELECT * FROM workers WHERE strftime('%d', dt2) = 3
""")
con.commit()
print(c.fetchall())

# 23
c.execute("""SELECT * FROM workers WHERE (strftime('%d', dt2) = '5') AND (strftime('%m', dt2) = '4')
""")
con.commit()
print(c.fetchall())

# 24
c.execute("""SELECT * FROM workers WHERE strftime('%d', dt2) IN (1, 7, 11, 12, 15, 19, 21, 23, 29)
""")
con.commit()
print(c.fetchall())

# 25
c.execute("""SELECT * FROM workers WHERE strftime('%w', dt2) = 2
""")
con.commit()
print(c.fetchall())

# 26
c.execute("""SELECT * FROM workers WHERE (strftime('%d', dt2) BETWEEN '1' AND '10') AND (strftime('%y', dt2) = '2016')
""")
con.commit()
print(c.fetchall())

# 27
c.execute("""SELECT * FROM workers WHERE strftime('%d', dt2) < strftime('%m', dt2)
""")
con.commit()
print(c.fetchall())

# 28
c.execute("""SELECT strftime('%Y', dt), strftime('%m', dt), strftime('%d',dt) FROM Workers
""")
con.commit()
print(c.fetchall())

# 29
c.execute("""SELECT strftime('%w', dt2) AS today FROM workers
""")
con.commit()
print(c.fetchall())

# 30
c.execute("""SELECT *, strftime('%d', dt2) AS d, strftime('%m', dt2) AS m, strftime('%Y', dt2) AS year FROM workers
""")
con.commit()
print(c.fetchall())

# 31
c.execute("""SELECT DATE(dt) AS date FROM workers
""")
con.commit()
print(c.fetchall())

# 32
c.execute("""SELECT strftime(dt2, '%d.%m.%Y ') as new_date FROM workers
""")
con.commit()
print(c.fetchall())

# 33
c.execute("""SELECT strftime(dt2, '%Y%%d.%m') AS new_date FROM workers
""")
con.commit()
print(c.fetchall())

# 34
c.execute('SELECT datetime(dt, "day + 1") AS date1 FROM Workers')
con.commit()
print(c.fetchall())

# 35
c.execute("""
SELECT datetime(dt, "day - 1") AS date1 FROM Workers
""")
con.commit()
print(c.fetchall())

# 36
c.execute("""
SELECT datetime(dt, "day +1", "hour + 2") AS date1 FROM Workers
""")
con.commit()
print(c.fetchall())

# 37
c.execute("""
SELECT datetime(dt, "year +1", "month + 2") AS date1 FROM Workers
""")
con.commit()
print(c.fetchall())

# 38
c.execute("""
SELECT datetime(dt, "day +1", "hour + 2", "minute +3") AS date1 FROM Workers
""")
con.commit()
print(c.fetchall())

# 39
c.execute("""
SELECT datetime(dt, "day + 1", "hour + 2", "minute + 3", " second + 5") AS date1 FROM Workers
""")
con.commit()
print(c.fetchall())

# 40
c.execute("""
SELECT datetime(dt, "hour + 2", "minute + 3", "second + 5") AS date1 FROM Workers
""")
con.commit()
print(c.fetchall())

# 41
c.execute("""
SELECT datetime(dt, "day + 1", "hour - 2") AS date1 FROM Workers
""")
con.commit()
print(c.fetchall())

# 42
c.execute("""
SELECT datetime(dt, "day + 1", "hour - 2", "minute - 3") AS date1 FROM Workers
""")
con.commit()
print(c.fetchall())

# 43
c.execute("""
SELECT *, 3 AS res FROM workers
""")
con.commit()
print(c.fetchall())

# 44
c.execute("""
SELECT *, 'eee' AS res FROM workers
""")
con.commit()
print(c.fetchall())

# 45
c.execute("""
SELECT *, 3 AS '3' FROM workers
""")
con.commit()
print(c.fetchall())

# 46
c.execute("""
SELECT *, (salary + age) AS res FROM workers
""")
con.commit()
print(c.fetchall())

# 47
c.execute("""
SELECT *, (salary - age) AS res FROM workers
""")
con.commit()
print(c.fetchall())

# 48
c.execute("""
SELECT *, (salary * age) AS res FROM workers
""")
con.commit()
print(c.fetchall())

# 49
c.execute("""
SELECT *, (salary + age) / 2 AS res FROM workers
""")
con.commit()
print(c.fetchall())

# 50
c.execute("""
SELECT * FROM workers WHERE (CAST(strftime('%d', dt2) AS INTEGER) + CAST(strftime('%m', dt2) AS INTEGER)) < 10
""")
con.commit()
print(c.fetchall())

# 51
c.execute("""
SELECT  SUBSTR(description, -1, -6) AS res FROM workers
""")
con.commit()
print(c.fetchall())

# 52
c.execute("""
SELECT  SUBSTR(description, -1, -6) AS res FROM workers
""")
con.commit()
print(c.fetchall())

# 53
c.execute("""
SELECT  SUBSTR(description, 2, 8) AS res FROM workers
""")
con.commit()
print(c.fetchall())

# # 54
# c.execute("""
# SELECT id, name FROM category UNION SELECT id, name FROM sub_category
# """)
# con.commit()
# print(c.fetchall())

# 55
c.execute("""
SELECT *, salary || age AS res FROM workers
""")
con.commit()
print(c.fetchall())

# 56
c.execute("""
SELECT *, salary || age || "!!!" AS res FROM workers
""")
con.commit()
print(c.fetchall())

# 57
c.execute("""
SELECT *, salary || "-" || age AS res FROM workers
""")
con.commit()
print(c.fetchall())

# 58
c.execute("""
SELECT *, SUBSTR(login, 0, 5) || "..." AS res FROM workers
""")
con.commit()
print(c.fetchall())

# 59
c.execute("""
SELECT age, MIN(salary) FROM workers GROUP BY age
""")
con.commit()
print(c.fetchall())

# 60
c.execute("""
SELECT salary, MAX(age) FROM workers GROUP BY salary
""")
con.commit()
print(c.fetchall())

# 61
c.execute("""

""")
con.commit()
print(c.fetchall())

# 62
c.execute("""
SELECT * FROM Workers WHERE salary > (SELECT AVG(salary) FROM Workers)
""")
con.commit()
print(c.fetchall())

# 63
c.execute("""
SELECT * FROM Workers WHERE age < ((SELECT AVG(age) FROM workers) /2*3)
""")
con.commit()
print(c.fetchall())

# 64
c.execute("""
SELECT * FROM Workers WHERE salary = (SELECT MIN(salary) FROM workers)
""")
con.commit()
print(c.fetchall())

# 65
c.execute("""
SELECT * FROM Workers WHERE salary = (SELECT MAX(salary) FROM workers)
""")
con.commit()
print(c.fetchall())
#
# # 66
# c.execute("""
# SELECT  MAX(salary) AS max WHERE age = 25
# """)
# con.commit()
# print(c.fetchall())

# 67
c.execute("""
SELECT ((SELECT MAX(age) FROM Workers) - (SELECT MIN(age) FROM Workers))/2 FROM Workers
""")
con.commit()
print(c.fetchall())

# 68
c.execute("""
SELECT ((SELECT MAX(age) FROM workers WHERE age=25) - (SELECT MIN(age) FROM workers WHERE age = 25))/2 FROM workers
""")
con.commit()
print(c.fetchall())

# 69
c.execute("""

""")
con.commit()
print(c.fetchall())

# 70
c.execute("""

""")
con.commit()
print(c.fetchall())

c.close()
con.close()

# 71

co1 = sqlite3.connect("test1.db")
c1 = co1.cursor()

co2 = sqlite3.connect("test2.db")
c2 = co2.cursor()



# # 72
# c2.execute("""
# DROP DATABASE IF EXISTS test2
# """)
# co2.commit()


# 73
c1.execute("""
CREATE TABLE table1(
    id INT AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(35),
    salary INT,
    age INT,
    date DATE
)
""")
co1.commit()
c1.execute("""
CREATE TABLE table2(
    id INT AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(35),
    salary INT,
    age INT,
    date DATE
)
""")
co1.commit()

# 74
c1.execute("""
ALTER TABLE table2 RENAME TO table3
""")
co1.commit()

# 75
c1.execute("""
DROP TABLE table3
""")
co1.commit()

# 76
c1.execute("""
ALTER TABLE table1 ADD status VARCHAR(35)
""")
co1.commit()

# 77
c1.execute("""
ALTER TABLE table1 DROP age
""")
co1.commit()

# 78
c1.execute("""
ALTER TABLE table1 CHANGE login user_login VARCHAR(35)
""")
co1.commit()

# 79
c1.execute("""
ALTER TABLE table1 CHANGE salary salary VARCHAR(255)
""")
co1.commit()

# 80
c1.execute("""
DELETE FROM table1
""")
co1.commit()

# 81
c1.execute("""
delete from test1 where type = 'table'
""")
co1.commit()

c1.close()
co1.close()
c2.close()
co2.close()

