import mysql.connector


myconn = mysql.connector.connect(
    host="localhost" ,
    user = "root" ,
    passwd = "toor" , 
    database='mydatabase'
)

mycursor = myconn.cursor()



sql = "INSERT INTO movies(name , plot) VALUES(%s , %s)"
data = [
    ("Preson Break2" , 'escape plan') ,
    ("vikins2" , 'old heros'),
    ]


mycursor.executemany(sql , data)

myconn.commit()

print('data inserted ')
print(mycursor.lastrowid)

