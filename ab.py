import pandas as pd
import pymysql
  
#Create the connection object   
myconn = pymysql.connect(host = "localhost", user = "root",passwd = "sweety110", database='lms', autocommit = True, charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor)

cursor = myconn.cursor() 


#cursor.execute('CREATE TABLE IF NOT Exists pro(product_name varchar(100),price int)')
#cursor.commit()

data={'product_name':['com','tab','monitor'],
'price':[100,200,300]}

df=pd.DataFrame(data,columns=['product_name','price'])
df.to_sql('pro',myconn,if_exists='replace',index=False)

c.execute('''
select * from pro''')


for row in c.fetchall():
	print(row)