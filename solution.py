import requests
import bs4
import pandas as pd

res = requests.get('http://www.three.co.uk/support/roaming/brazil')

soup = bs4.BeautifulSoup(res.text, 'lxml')

datalist = []

# get the table
table = soup.select("table")
# convert the table into a data frame using pandas
df = pd.read_html(str(table), header=0)
# append data to data list
datalist.append(df[0])

print(datalist)
