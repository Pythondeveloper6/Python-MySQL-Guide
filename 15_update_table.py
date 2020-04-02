import mysql.connector


myconn = mysql.connector.connect(
    host="localhost" ,
    user = "root" ,
    passwd = "toor" , 
    database='mydatabase'
)

mycursor = myconn.cursor()



# mycursor.execute("UPDATE movies SET plot = 'using the update statement' WHERE name='vikins'")
mycursor.execute("UPDATE movies SET plot = 'using the update statement' ")

myconn.commit()





