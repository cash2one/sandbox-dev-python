#!/usr/local/bin/python
#encoding:utf-8
import sqlite3

conn = sqlite3.connect(':memory:')
curr = conn.cursor()
conn.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
curr.execute('''select name from sqlite_master where type='table' order by name;''')
print 'all tables:', curr.fetchall()

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

conn.executemany("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (?, ?, ?, ?, ?)",
        [(2, 'Allen', 25, 'Texas', 15000.00 ), (3, 'Xiaoming', 27, 'TT', 18000.00 )]);

conn.executescript('''INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Paul', 32, 'California', 20000.00 );
      INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (5, 'Paul', 32, 'California', 20000.00 )''')

conn.commit()

cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
print 'fetchall', cursor.fetchall()
print 'fetch one', cursor.fetchone()
print 'fetchmany', cursor.fetchmany(2)
for row in cursor:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"

conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
conn.commit
print "Total number of rows updated :", conn.total_changes

conn.close()