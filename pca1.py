import pymysql
  
#Create the connection object   
myconn = pymysql.connect(host = "localhost", user = "root",passwd = "sweety110", database='lms', autocommit = True, charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor)

cursor = myconn.cursor() 


sql = "create table reservation (reservationID varchar2(10),airlinesName varchar2(100),capacityofpassenger int,boardingat varchar2(100),destination varchar2(100));"
cursor.execute(sql)

#rows = cursor.fetchall()

#print(rows)


sql = "insert into reservation (reservationID,airlinesName,capacityofpassenger,boardingat,destination) values (%s, %s,%s,%s,%s)"
val = [("a1","Indigo", 100,"Delhi","kolkata"),
       ("b1","ABC", 200,"mumbai","delhi"),
      ("c1","AC", 10,"kolkata","xfhh"),
      ("d1","AB", 180,"Delhi","chennai"),
      ("e1","ABC", 180,"kolkata","delhi"),
      ("f1","BC", 190,"Delhi","us"),
      ("g1","BC", 107,"Delhi","loc"),
      ("h1","hBC", 105,"kolkata","rtrs"),
      ("i1","BC", 107,"durgapur","kolkata"),
      ("j1","xy", 101,"Delhi","kolkata")]
cursor.execute(sql, val)

myconn.commit()

print(cursor.rowcount, "record inserted.")



sql = "select * from reservation"
cursor.execute(sql)

rows = cursor.fetchall()

print(rows)