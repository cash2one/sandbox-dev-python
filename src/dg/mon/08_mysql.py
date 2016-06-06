#!/usr/local/bin/python
#coding=utf-8
import MySQLdb

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='123456',
        db ='test',
        )
cur = conn.cursor()

#创建数据表
cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

#插入一条数据
cur.execute("insert into student values('2','Tom','3 year 2 class','9')")

sqli="insert into student values(%s,%s,%s,%s)"
cur.execute(sqli,('3','Huhu','2 year 1 class','7'))

sqli="insert into student values(%s,%s,%s,%s)"
cur.executemany(sqli,[
    ('3','Tom','1 year 1 class','6'),
    ('3','Jack','2 year 1 class','7'),
    ('3','Yaheng','2 year 2 class','7'),
    ])

#修改查询条件的数据
print cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

#删除查询条件的数据
print cur.execute("delete from student where age='9'")

total=cur.execute("select * from student")
print total
info = cur.fetchmany(total)
for ii in info:
    print ii

cur.close()
conn.commit()
conn.close()