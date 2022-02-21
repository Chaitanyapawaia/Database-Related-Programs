import mysql.connector as sqltor
mycon = sqltor.connect(host = "localhost", user="root", passwd="ol9E", database="Class12program")
if mycon.is_connected() == False:
    print("Error connecting to MYSQL database")
cursor = mycon.cursor()
w=int(input("Enter the number of lines:"))
cursor.execute("select * from pythonread")
data = cursor.fetchmany(w)
count = cursor.rowcount 
for row in data :
    print(row)
mycon.close()

