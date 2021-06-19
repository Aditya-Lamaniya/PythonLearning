import mysql.connector;

connection = mysql.connector.connect(host='127.0.0.1', database='mydb', user='root', password='Aditya@29')
if connection.is_connected():
    print("connection succesful")

cursor=connection.cursor()
print("debug 1 ")
#cursor.execute("create table emp_1(id int,name varchar(50),sal int)")

try :
    cursor.execute("insert into emp_1 values(1,'ai',100)")
    print("debug 2 ")
    connenamection.commit()
    print("debug 3 ")
except:
    connection.rollback()
    print("debug 4")

cursor.close()
connection.close()
print("debug 5")