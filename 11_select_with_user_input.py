import mysql.connector


myconn = mysql.connector.connect(
    host="localhost" ,
    user = "root" ,
    passwd = "toor" , 
    database='mydatabase'
)

mycursor = myconn.cursor()

sql = " SELECT * FROM movies WHERE name=%s "
data = ('vikins',)

mycursor.execute(sql , data)



result = mycursor.fetchall()

print(result)





