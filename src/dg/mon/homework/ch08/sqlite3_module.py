#!/usr/local/bin/python
# encoding:utf-8
import sqlite3
import itertools
import os


def read():
    # conn = sqlite3.connect(':memory:')
    conn = sqlite3.connect('output.sqllite3')
    curr = conn.cursor()
    conn.execute('''CREATE TABLE COMPANY
           (ID INT PRIMARY KEY     NOT NULL,
           NAME           TEXT    NOT NULL,
           AGE            INT     NOT NULL,
           ADDRESS        CHAR(50),
           SALARY         REAL);''')
    curr.execute('''SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;''')
    # print('all tables:', curr.fetchall())

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (1, 'Paul', 32, 'California', 20000.00 )");

    conn.executemany("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (?, ?, ?, ?, ?)",
                     [(2, 'Allen', 25, 'Texas', 15000.00), (3, 'Xiaoming', 27, 'TT', 18000.00)]);

    conn.executescript('''INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Paul', 32, 'California', 20000.00 );
          INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (5, 'Paul', 32, 'California', 20000.00 )''')

    conn.commit()

    cursor = conn.execute("SELECT id, name, address, salary  FROM COMPANY")
    # print('fetchall', cursor.fetchall())
    # print 'fetch one', cursor.fetchone()
    # print 'fetchmany', cursor.fetchmany(2)
    # for row in cursor:
    #   print("ID = ", row[0])
    #   print("NAME = ", row[1])
    #   print("ADDRESS = ", row[2])
    #   print("SALARY = ", row[3], "\n")

    conn.execute("UPDATE COMPANY SET SALARY = 25000.00 WHERE ID=1")
    conn.commit
    # print("Total number of rows updated :", conn.total_changes)

    conn.close()


def write(filepath):
    # conn = sqlite3.connect(':memory:')
    conn = sqlite3.connect(filepath)
    curr = conn.cursor()
    conn.execute('''CREATE TABLE COMPANY
           (ID INT PRIMARY KEY     NOT NULL,
           NAME           TEXT    NOT NULL,
           AGE            INT     NOT NULL,
           ADDRESS        CHAR(50),
           SALARY         REAL);''')
    curr.execute('''SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;''')
    # print('all tables:', curr.fetchall())

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (1, 'Paul', 32, 'California', 20000.00 )");

    conn.executemany("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (?, ?, ?, ?, ?)",
                     [(2, 'Allen', 25, 'Texas', 15000.00), (3, 'Xiaoming', 27, 'TT', 18000.00)]);

    conn.executescript('''INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Paul', 32, 'California', 20000.00 );
          INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (5, 'Paul', 32, 'California', 20000.00 )''')

    conn.commit()

    cursor = conn.execute("SELECT id, name, address, salary  FROM COMPANY")
    # print('fetchall', cursor.fetchall())
    # print 'fetch one', cursor.fetchone()
    # print 'fetchmany', cursor.fetchmany(2)
    # for row in cursor:
    #   print("ID = ", row[0])
    #   print("NAME = ", row[1])
    #   print("ADDRESS = ", row[2])
    #   print("SALARY = ", row[3], "\n")

    conn.execute("UPDATE COMPANY SET SALARY = 25000.00 WHERE ID=1")
    conn.commit
    # print("Total number of rows updated :", conn.total_changes)

    conn.close()


def get_fetchall_data(filepath, sql):
    # conn = sqlite3.connect(':memory:')
    conn = sqlite3.connect(filepath)
    cursor = conn.cursor()
    cursor.execute(sql)
    result_list = cursor.fetchall()
    conn.close()
    return (result_list)


def get_table_list(filepath):
    return (get_fetchall_data(filepath, '''select name from sqlite_master where type='table' order by name;'''))


def get_table_info(filepath, tablename):
    return (get_fetchall_data(filepath, '''pragma table_info(''' + tablename + ''')'''))


def get_table_data(filepath, tablename):
    return (get_fetchall_data(filepath, '''select * from ''' + tablename + ''))


def remove_file(filepath):
    try:
        os.remove(filepath)
    except OSError:
        pass


def extract_data(sqlite_filepath):

    table_list = get_table_list(sqlite_filepath)
    table_list = list(itertools.chain(*table_list))
    # table_list = list(itertools.chain(get_table_list('output.sqllite3'))
    # print(table_list)
    
    create_statments = []
    insert_statments = []
    for table_name in table_list:
        column_infos = get_table_info(sqlite_filepath, table_name)
        create_statment = "create table {0} (".format(table_name);
        
        for column_info in column_infos:
            create_statment = create_statment + '{0} {1}, '.format(column_info[1], column_info[2])
        create_statments.append(create_statment[0:len(create_statment) - 2] + " );")

        records = get_table_data(sqlite_filepath, table_name)
        for record in records:
            insert_statment = "insert into {0} values ( ".format(table_name);
            for column_data in record:
                # print(type(column_data))
                if type(column_data) is unicode:
                    insert_statment = insert_statment + '\'{0}\', '.format(column_data)
                if type(column_data) in (int, float):
                    insert_statment = insert_statment + '{0}, '.format(column_data)
            insert_statments.append(insert_statment[0:len(insert_statment) - 2] + " ) ;")
        # print(records)

    # print(create_statments)
    # print(insert_statments)
    return(create_statments+insert_statments)


def load_data(sqlite_filepath, statments):
    conn = sqlite3.connect(sqlite_filepath)
    for statment in statments:
        print(statment)
        conn.execute(statment)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    fromDict = {'type': 'sqlite', 'connect_paramters': 'test.sqlite3'}
    
    sqlite_filepath = fromDict['connect_paramters']
    
    # reset test data    
    remove_file(sqlite_filepath)
    write(sqlite_filepath)

    result = extract_data(sqlite_filepath)
    print(result)
