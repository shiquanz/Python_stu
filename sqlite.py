#! /usr/bin/python
#coding:utf-8

import sqlite3

#连接数据库 , 如果不存在则创建
conn = sqlite3.connect('test.db')

print "Opened databases successfully"

#如果表company存在 则删除!
#conn.execute('''drop table if exists company;''')

#-------------创建表
sql_create_table = '''
	create table company
	(id int primary key not NULL ,
	name text not null ,
	age int not null,
	address char(50) ,
	salary real);
	'''
#conn.execute(sql_create_table)

#--------------插入数据
sql_insert = '''
insert into company (id , name , age , address , salary)
values(3 , 'Paul' , 32 , 'California' , 2000.0);
'''
#conn.execute(sql_insert)
#conn.commit()
print "records created successfully!"

#--------------查询数据
sql_select = '''
select id , name  , address , salary from company;
'''
cursor = conn.execute(sql_select)
for row in cursor:
	print "ID=",row[0]
	print "name=",row[1]
	print "address=",row[2]
	print "salary=",row[3]

#---------------更改数据
sql_update = '''
update company set salary = 33333 where id=1;
'''
conn.execute(sql_update)
conn.commit


#---------------删除数据
sql_delete  = '''
delete from company where id=2;
'''
conn.execute(sql_delete)
conn.commit


#---------------关闭数据库连接
conn.close()
