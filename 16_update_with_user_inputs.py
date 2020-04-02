import mysql.connector


myconn = mysql.connector.connect(
    host="localhost" ,
    user = "root" ,
    passwd = "toor" , 
    database='mydatabase'
)

mycursor = myconn.cursor()



sql = "UPDATE movies SET plot =%s WHERE name=%s"
data = ('using user inputs' , 'vikins')

mycursor.execute(sql,data)

myconn.commit()





