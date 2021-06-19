import mysql.connector as my
try:
    connection = my.connect(host='127.0.0.1', database='mydb', user='root', password='Aditya@29')

    if connection.is_connected():
        print("connection successful ")

    cursor = connection.cursor()
    cursor.execute("select * from emp")
    row = cursor.fetchone()

    while row is not None:
        print(row)
        row = cursor.fetchone()

    cursor.close()
    connection.close()
except my.Error as e:
    print(e)
