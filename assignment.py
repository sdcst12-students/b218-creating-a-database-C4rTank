#!python3

import sqlite3

file = 'dbase.db'
connection = sqlite3.connect(file)
print(connection)

cursor = connection.cursor()

query = ('''
    create table if not exists veterinarian (
    id integer primary key autoincrement,
    fname TINYTEXT,
    lname TINYTEXT,
    phone BIT,
    email TINYTEXT,
    address TINYTEXT,
    city TINYTEXT,
    postalcode TINYTEXT);
''')

cursor.execute(query)
data = [

    ]

for i in data:
    query = f"insert into veterinarian (id,fname,lname,phone,email,address,city,postalcode) values ('{i[0]}','{i[1]}','{i[2]}','{i[3]}','{i[4]}','{i[5]}','{i[6]}','{i[7]}');"
    print(query)
    cursor.execute(query)
connection.commit()
query = "select * from veterinarian"
cursor.execute(query)
result = cursor.fetchall()
print(result)
for i in result:
    print('(------------------------------------------------------------------------------)')
    print(i)
print('(------------------------------------------------------------------------------)')
print('.\sqlite3 dbase.db')
