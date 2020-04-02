import mysql.connector


myconn = mysql.connector.connect(
    host="localhost" ,
    user = "root" ,
    passwd = "toor" , 
    # database = 'cars'
)

mycursor = myconn.cursor()



print('COnnected ')
mycursor.execute("SHOW DATABASES")