import pandas as pd


# Import CSV
data = pd.read_csv (r'C:\Users\HP\Desktop\Machine learning\Position_Salaries.csv')   
df = pd.DataFrame(data)
print(df.head())

import pymysql
  
#Create the connection object   
myconn = pymysql.connect(host = "localhost", user = "root",passwd = "sweety110", database='lms', autocommit = True, charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor)

cursor = myconn.cursor() 

# Create Table
cursor.execute('''
		CREATE TABLE emp (
			Position varchar(100),
			Level varchar(50),
			Salary int
			)
               ''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO emp (Position, Level,Salary)
                VALUES (?,?,?)
                ''',
                row.Position, 
                row.Level,
                row.Salary
                )
conn.commit()