import mysql.connector as sqltor
mycon = sqltor.connect(host = "localhost", user="root", passwd="ol9E", database="Class12program")
if mycon.is_connected() == False:
    print("Error connecting to MYSQL database")
cursor = mycon.cursor()
cursor.execute("select * from pythonread")
data = cursor.fetchall()
count = cursor.rowcount 
for row in data :
    print(row)
mycon.close()
