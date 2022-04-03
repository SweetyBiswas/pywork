
# import mysql.connector
import pymysql
import pandas as pd
df=pd.read_csv(r'C:\Users\HP\Desktop\Machine learning\Position_Salaries.csv')

print(df)

#Create the connection object   
myconn = pymysql.connect(host = "localhost", user = "root",passwd = "sweety110", database='lms', autocommit = True, charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor)

cursor = myconn.cursor() 

from sqlalchemy import create_engine
# engine = create_engine('sqlite://', echo=False)
engine = create_engine("mysql+pymysql://root:sweety110@localhost/lms")

df.to_sql('users', con=engine)
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())
# myconn.commit()


