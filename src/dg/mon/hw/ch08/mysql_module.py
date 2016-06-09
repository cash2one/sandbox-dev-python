#!/usr/local/bin/python
# coding=utf-8
import MySQLdb
import itertools


def read():
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='',
        db='test',
    )
    cur = conn.cursor()

    # 创建数据表
    cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

    # 插入一条数据
    cur.execute("insert into student values('2','Tom','3 year 2 class','9')")

    sqli = "insert into student values(%s,%s,%s,%s)"
    cur.execute(sqli, ('3', 'Huhu', '2 year 1 class', '7'))

    sqli = "insert into student values(%s,%s,%s,%s)"
    cur.executemany(sqli, [
        ('3', 'Tom', '1 year 1 class', '6'),
        ('3', 'Jack', '2 year 1 class', '7'),
        ('3', 'Yaheng', '2 year 2 class', '7'),
    ])

    # 修改查询条件的数据
    print cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

    # 删除查询条件的数据
    print cur.execute("delete from student where age='9'")

    total = cur.execute("select * from student")
    print total
    info = cur.fetchmany(total)
    for ii in info:
        print ii

    cur.execute("drop table student")

    cur.close()
    conn.commit()
    conn.close()


def write():
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='',
        db='test',
    )
    cur = conn.cursor()

    # 创建数据表
    cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

    # 插入一条数据
    cur.execute("insert into student values('2','Tom','3 year 2 class','9')")

    sqli = "insert into student values(%s,%s,%s,%s)"
    cur.execute(sqli, ('3', 'Huhu', '2 year 1 class', '7'))

    sqli = "insert into student values(%s,%s,%s,%s)"
    cur.executemany(sqli, [
        ('3', 'Tom', '1 year 1 class', '6'),
        ('3', 'Jack', '2 year 1 class', '7'),
        ('3', 'Yaheng', '2 year 2 class', '7'),
    ])

    # 修改查询条件的数据
    print cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

    # 删除查询条件的数据
    print cur.execute("delete from student where age='9'")

    total = cur.execute("select * from student")
    print total
    info = cur.fetchmany(total)
    for ii in info:
        print ii

    cur.execute("drop table student")

    cur.close()
    conn.commit()
    conn.close()


def get_fetchall_data(conn, sql):
    print(sql)
    result_list = cur.fetchmany(cur.execute(sql))
    return(result_list)


def get_table_list(conn):
    return(get_fetchall_data(conn, 'show tables;'))


def get_table_info(conn, tablename):
    return(get_fetchall_data(conn, 'select COLUMN_NAME,data_type from information_schema.COLUMNS where table_name = \'' + tablename + '\';'))


def get_table_data(conn, tablename):
    return(get_fetchall_data(conn, '''select * from ''' + tablename + ''))


if __name__=="__main__":
    # read()
    # write()
    fromDict = {'type' : 'mysql', 'connect_paramters' : {'host':'localhost', 'username':'root', 'password':'mysql', 'port':'3306', 'dbname':'test'}}
    sqlite_filepath = fromDict['connect_paramters']
    conn= MySQLdb.connect(
        host = fromDict['connect_paramters']['host'],
        port = int(fromDict['connect_paramters']['port']),
        user=fromDict['connect_paramters']['username'],
        passwd=fromDict['connect_paramters']['password'],
        db =fromDict['connect_paramters']['dbname'],
        )
    cur = conn.cursor()
    table_list = get_table_list(conn)
    table_list = list(itertools.chain(*table_list))
    print(table_list)
    # table_list = list(itertools.chain(get_table_list('output.sqllite3'))
    # print(table_list)
    create_statments = []
    insert_statments = []
    for table_name in table_list:
        print(table_name)
        column_infos = get_table_info(conn, table_name)
        print(column_infos)
        create_statment = "create table {0} (".format(table_name);
        insert_statment = "insert into {0} values ( ".format(table_name);
        for column_info in column_infos:
          create_statment = create_statment + '{0} {1}, '.format(column_info[0], column_info[1])
        create_statments.append(create_statment[0:len(create_statment)-2] + " );")
        records = get_table_data(conn, table_name)
        for record in records:
          # insert_statment = insert_statment + '{0}, '.format(column_info[1], column_info[2])
          for column_data in record:
            print(type(column_data))
            if type(column_data) in (unicode,str):
              insert_statment = insert_statment + '\'{0}\' , '.format(column_data)
            if type(column_data) in (int, float,long):
              insert_statment = insert_statment + '{0}, '.format(column_data)
          # insert_statment = ', '.join(record)
          insert_statments.append(insert_statment[0:len(insert_statment)-2] + " ) ;")
        print(records)
    print(create_statments)
    print(insert_statments)
    conn.close()
