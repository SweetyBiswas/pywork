from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

# req=requests.get("https://www.flipkart.com/apple-iphone-12-black-64-gb/p/itma2559422bf7c7?pid=MOBFWBYZU5FWK2VP&lid=LSTMOBFWBYZU5FWK2VPUYA8BN&marketplace=FLIPKART&q=APPLE+iPhone+12+%28Black%2C+64+GB%29&store=tyy%2F4io&srno=s_1_1&otracker=AS_Query_HistoryAutoSuggest_2_0&otracker1=AS_Query_HistoryAutoSuggest_2_0&fm=SEARCH&iid=631df036-352b-4c55-ad13-feceba66ae3f.MOBFWBYZU5FWK2VP.SEARCH&ppt=hp&ppn=homepage&ssid=pqcwx4jh6o0000001636295316165&qH=0fde1790d08e1a1a")
# soup=BeautifulSoup(req.content,"html.parser")

# #print(soup.get_text())

# x=soup.Specifications
# print(x.get_text())


General=[]
# Display_Features=[]
# ModelName=[]
# Color=[]
# price=[]
req=requests.get("https://www.flipkart.com/apple-iphone-12-black-64-gb/p/itma2559422bf7c7?pid=MOBFWBYZU5FWK2VP&lid=LSTMOBFWBYZU5FWK2VPUYA8BN&marketplace=FLIPKART&q=APPLE+iPhone+12+%28Black%2C+64+GB%29&store=tyy%2F4io&srno=s_1_1&otracker=AS_Query_HistoryAutoSuggest_2_0&otracker1=AS_Query_HistoryAutoSuggest_2_0&fm=SEARCH&iid=631df036-352b-4c55-ad13-feceba66ae3f.MOBFWBYZU5FWK2VP.SEARCH&ppt=hp&ppn=homepage&ssid=pqcwx4jh6o0000001636295316165&qH=0fde1790d08e1a1a")
soup=BeautifulSoup(req.content,"html.parser")


General=soup.find('div',attrs={'class':'_3k-BhJ'})

#product=soup.find('li',attrs={'XPath':'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[9]/div[6]/div/div[2]/div[1]/div[1]/table/tbody/tr[6]/td[2]/ul/li'})
x=General.get_text()
print(x)

import pymysql
myconn = pymysql.connect(host = "localhost", user = "root",passwd = "sweety110", database='lms', autocommit = True, charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor)

cursor = myconn.cursor() 

cursor.execute("CREATE TABLE Specifications1 (General VARCHAR(500))")



sql = "INSERT INTO Specifications1 (General) VALUES (%s)"
records_to_insert = x
cursor.execute(sql, records_to_insert)

myconn.commit()

# mySql_insert_query = """INSERT INTO WIKI2 (RANKING, MARKET, RETAIL_VALUE, PHYSICAL,DIGITAL,PERFORMANCE_RIGHTS,SYNCHRONIZATION) 
# VALUES (%s, %s, %s, %s ,%s, %s, %s) """




# cursor = scrap_db.cursor()
# cursor.executemany(sql, records_to_insert)
# scrap_db.commit()














# Display_Features=soup.find('div',attrs={'class':'_21lJbe'})

# print(Display_Features.get_text())




#B_NucI
# import bs4
# import urllib.request
# from urllib.request import urlopen
# from bs4 import BeautifulSoup as soup

# #Go to webpage and scrape data

# html = urlopen('https://www.flipkart.com/apple-iphone-12-black-64-gb/p/itma2559422bf7c7?pid=MOBFWBYZU5FWK2VP&lid=LSTMOBFWBYZU5FWK2VPUYA8BN&marketplace=FLIPKART&q=APPLE+iPhone+12+%28Black%2C+64+GB%29&store=tyy%2F4io&srno=s_1_1&otracker=AS_Query_HistoryAutoSuggest_2_0&otracker1=AS_Query_HistoryAutoSuggest_2_0&fm=SEARCH&iid=631df036-352b-4c55-ad13-feceba66ae3f.MOBFWBYZU5FWK2VP.SEARCH&ppt=hp&ppn=homepage&ssid=pqcwx4jh6o0000001636295316165&qH=0fde1790d08e1a1a')
# bsobj = soup(html.read())
# print(bsobj)
# # tbody = bsobj('table',{'class':'wikitableplainrowheaders sortable'})[0].findAll('tr')
# # xl = []
# # for row in tbody:
# #   cols = row.findChildren(recursive = False)
# #   cols = tuple(element.text.strip().replace('%','') for element in cols)
# #   xl.append(cols)
# # xl = xl[1:-1]
# # print(xl)






# driver = webdriver.Chrome(r"C:\Users\HP\Downloads\chromedriver_win32 (2)\chromedriver.exe")
# driver.get("https://www.flipkart.com")

# driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input').send_keys('sweetybiswas2927@gmail.com')




# req=requests.get("https://www.flipkart.com/apple-iphone-12-black-64-gb/p/itma2559422bf7c7?pid=MOBFWBYZU5FWK2VP&lid=LSTMOBFWBYZU5FWK2VPUYA8BN&marketplace=FLIPKART&q=APPLE+iPhone+12+%28Black%2C+64+GB%29&store=tyy%2F4io&srno=s_1_1&otracker=AS_Query_HistoryAutoSuggest_2_0&otracker1=AS_Query_HistoryAutoSuggest_2_0&fm=SEARCH&iid=631df036-352b-4c55-ad13-feceba66ae3f.MOBFWBYZU5FWK2VP.SEARCH&ppt=hp&ppn=homepage&ssid=pqcwx4jh6o0000001636295316165&qH=0fde1790d08e1a1a")
# soup=BeautifulSoup(req.content,"html.parser")

# #print(soup.get_text())

# x=soup.title
# print(x.prettify())