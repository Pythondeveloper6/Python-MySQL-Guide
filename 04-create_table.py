import mysql.connector


myconn = mysql.connector.connect(
    host="localhost" ,
    user = "root" ,
    passwd = "toor" , 
    database='mydatabase'
)

mycursor = myconn.cursor()


mycursor.execute("  CREATE TABLE movies (name VARCHAR(100) , plot VARCHAR(500) )")

print('Table Created Successfully')

