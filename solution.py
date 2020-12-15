import requests
from selenium import webdriver
import bs4
import pandas as pd

url = "http://www.three.co.uk/Support/Roaming_and_international/Roaming_Abroad/Destinations?#countries2"

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)
Xpath = '//ul//li[@class="underline bold"]//a[@title="Brazil."]'
# python_button = driver.find_element_by_xpath(Xpath)
python_button = driver.find_element_by_link_text('Brazil.')
python_button.click()

# res = requests.get('http://www.three.co.uk/support/roaming/brazil')

soup = bs4.BeautifulSoup(driver.page_source, 'lxml')

datalist = []

# get the table
table = soup.select("table")
# convert the table into a data frame using pandas
df = pd.read_html(str(table), header=0)
# append data to data list
datalist.append(df[0])

print(datalist)
