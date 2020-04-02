import mysql.connector


myconn = mysql.connector.connect(
    host="localhost" ,
    user = "root" ,
    passwd = "toor" , 
    database='mydatabase'
)

mycursor = myconn.cursor()




# mycursor.execute("DELETE FROM movies WHERE name='vikins' ")


sql = "DELETE FROM movies WHERE name=%s "
data = ('vikins2',)

mycursor.execute(sql , data)


myconn.commit()





