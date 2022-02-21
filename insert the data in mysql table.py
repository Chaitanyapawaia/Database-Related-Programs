import mysql.connector as sqltor
mycon = sqltor.connect(host = "localhost", user="root", passwd="ol9E", database="Class12program")
if mycon.is_connected() == False:
    print("Error connecting to MYSQL database")
cursor = mycon.cursor()
st="INSERT INTO pythonread (Rollno, Name, Section, Marks) VALUES(5, 'Eka', 'A',100)"
cursor.execute(st)
mycon.commit()
mycon.close()
         