# import mysql.connector
import pymysql
  
#Create the connection object   
myconn = pymysql.connect(host = "localhost", user = "root",passwd = "sweety110", database='lms', autocommit = True, charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor)

cursor = myconn.cursor() 
#printing the connection object   
# print(myconn)  

sql = "select * from student"
cursor.execute(sql)

rows = cursor.fetchall()

print(rows)


sql = "INSERT INTO student (studentID,name,fatherName,coursename,branchName) VALUES (%s, %s,%s,%s,%s)"
val = (98,"XXXXXXXX", "XXXXXXX","XXXXXXXXX","XXXXXX")
cursor.execute(sql, val)

myconn.commit()

print(cursor.rowcount, "record inserted.")










cursor.execute("update student set name = 'XXXXXX' where studentID = 1")  
myconn.commit() 
myconn.close()  



#print(cursor.rowcount, "record(s) affected")




