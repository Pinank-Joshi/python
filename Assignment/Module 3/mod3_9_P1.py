import sqlite3

try:
    db=sqlite3.connect("testdb.db")
    print("Database connected!")
except Exception as e:
    print(e)

#Table Create
create_tbl="create table userinfo(id integer primary key autoincrement, name text, city text)"

try:
    db.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)

n=int(input("Enter number of User:"))
for i in range(n):
    name=input("Enter your name:")
    city=input("Enter your city:")
    insert_data=f"insert into userinfo(name,city)values('{name}','{city}')"
    
    try:
        db.execute(insert_data)
        db.commit()
        print("Resord Inserted!")
    except Exception as e:
        print(e)

#Show Data
cr=db.cursor()
show_data="select * from userinfo"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    for i in data:
        print(i)
except Exception as e:
    print(e)

