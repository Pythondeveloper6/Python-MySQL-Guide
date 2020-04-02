import mysql.connector


myconn = mysql.connector.connect(
    host="localhost" ,
    user = "root" ,
    passwd = "toor" , 
    database='mydatabase'
)

mycursor = myconn.cursor()



sql = "INSERT INTO movies(name , plot) VALUES(%s , %s)"
data = ("Harry Potter2" , 'magic Movie2')


mycursor.execute(sql , data)

myconn.commit()

print('data inserted ')
print(mycursor.lastrowid)

