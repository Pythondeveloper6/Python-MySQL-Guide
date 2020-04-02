import mysql.connector


myconn = mysql.connector.connect(
    host="localhost" ,
    user = "root" ,
    passwd = "toor" , 
    database='mydatabase'
)

mycursor = myconn.cursor()








mycursor.execute("DROP TABLE movies")
# mycursor.execute("DROP TABLE IF EXISTS movies")


myconn.commit()





