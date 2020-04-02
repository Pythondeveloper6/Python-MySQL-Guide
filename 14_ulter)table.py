import mysql.connector


myconn = mysql.connector.connect(
    host="localhost" ,
    user = "root" ,
    passwd = "toor" , 
    database='mydatabase'
)

mycursor = myconn.cursor()



# mycursor.execute(" ALTER TABLE movies ADD COLUMN language VARCHAR(30)")
mycursor.execute(" ALTER TABLE movies CHANGE language language VARCHAR(50)")
myconn.commit()





