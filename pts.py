
import pandas as pd
df=pd.read_csv(r'C:\Users\HP\Desktop\pyworks\heart_failure_clinical_records_dataset.csv')
#df=pd.read_csv("heart_failure_clinical_records_dataset")
print(df.head())


# import mysql.connector
import pymysql
  
#Create the connection object   
myconn = pymysql.connect(host = "localhost", user = "root",passwd = "sweety110", database='lms', autocommit = True, charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor)

cursor = myconn.cursor() 






cursor.execute('''CREATE TABLE heart_1 (age int,anaemia int,creatinine_phosphokinase int,diabetes int,ejection_fraction int,high_blood_pressure int,platelets int,serum_creatinine int,serum_sodium int,sex int,smoking int,time int,DEATH_EVENT int )''')




for row in df.itertuples():
    cursor.execute(
                "INSERT INTO heart_1 (age,anaemia,creatinine_phosphokinase,diabetes,ejection_fraction,high_blood_pressure,platelets,serum_creatinine,serum_sodium,sex,smoking,time,DEATH_EVENT) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                ,
                (row.age, 
                row.anaemia,
                row.creatinine_phosphokinase,
                row.diabetes, 
                row.ejection_fraction,
                row.high_blood_pressure,
                row.platelets, 
                row.serum_creatinine,
                row.serum_sodium,
                row.sex,
                row.smoking,
                row.time,
                row.DEATH_EVENT)
                )
myconn.commit()
