import mysql.connector


myconn = mysql.connector.connect(
    host="localhost" ,
    user = "root" ,
    passwd = "toor" , 
    # database = 'cars2'
)

mycursor = myconn.cursor()


mycursor.execute(" SHOW DATABASES")

for db in mycursor:
    print(db)