import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user="root",
    password='Root123@' ,
    database='demo_db'
)

if conn.is_connected():
    print("Connection successful")
else:
    print("Connection failed")

cursor=conn.cursor()
#create a table 'user'
cursor.execute('''
CREATE TABLE IF NOT EXISTS user(
    id integer PRIMARY KEY,
    name varchar(20) NOT NULL,
    age integer NOT NULL,
    Phone_Number  varchar(15) NOT NULL

)

''')


# collect user input
id=int(input("Enter user id:"))
name=input("Enter user name:")
age=int(input("Enter user age:"))
Phone_Number=input("Enter user Phone_Number:")
#city=input("Enter user city:")

#insert the user input into the 'user'table
cursor.execute('''
INSERT INTO user(id,name,age,Phone_Number)
    VALUES (%s,%s,%s,%s)
''',(id,name,age,Phone_Number))

conn.commit()

print("User data inserted successfully.")

# retrive and display all records
cursor.execute('SELECT * FROM user')
rows=cursor.fetchall()

print("\nALL users:")
for row in rows:
    print(row)

#close the database connection
conn.close()




