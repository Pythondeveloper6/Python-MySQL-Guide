import mysql.connector


myconn = mysql.connector.connect(
    host="localhost" ,
    user = "root" ,
    passwd = "toor" , 
    database='mydatabase'
)

mycursor = myconn.cursor()


# mycursor.execute(" SELECT * FROM movies LIMIT 5")
mycursor.execute(" SELECT * FROM movies LIMIT 5 OFFSET 2")


result = mycursor.fetchall()

print(result)





