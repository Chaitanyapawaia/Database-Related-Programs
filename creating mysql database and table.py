import mysql.connector as sqltor
mycon = sqltor.connect(host = "localhost", user="root", passwd="ol9E")
if mycon.is_connected() == False:
    print("Error connecting to MYSQL database")
cursor = mycon.cursor()
cursor.execute("CREATE DATABASE pythoninsert")
print("Database Created.")
mycon.close() 

conn = sqltor.connect(host = "localhost", user="root", passwd="ol9E", database='pythoninsert')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Dropping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#Creating table as per requirement
sql ='''CREATE TABLE EMPLOYEE(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT
)'''
cursor.execute(sql)
print("Table Created.")


conn.close()