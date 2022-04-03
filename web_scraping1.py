from selenium import webdriver
from bs4 import BeautifulSoup


# url = "https://www.flipkart.com"
# browser(url)
# print(browser)

# driver = webdriver.Chrome(r"C:\Users\HP\Downloads\chromedriver_win32 (2)\chromedriver.exe")
# driver.get("https://www.flipkart.com")

# #browser.get(url)

# html=browser.page_source
# print(html)

#browser = webdriver.Chrome(r"C:\webdriversr.exe")






import requests
from bs4 import BeautifulSoup
url = "https://www.flipkart.com"
r=requests.get(url)
htmlContent=r.content
#print(htmlContent)

soup = BeautifulSoup(htmlContent,'html.parser')
print(soup)


title=soup.title
print(type(soup))
print(type(title))
print(type(title.string))




