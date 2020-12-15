from selenium import webdriver
import bs4
import pandas as pd
import os

url = "http://www.three.co.uk/Support/Roaming_and_international/Roaming_Abroad/Destinations?#countries2"

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)

datalist = []
query = ["Brazil.", "South Africa.", "Portugal.",
         "Chile.", "Iceland.", "China.", "Madagascar."]

for country in query:
    python_button = driver.find_element_by_link_text(country)
    python_button.click()

    soup = bs4.BeautifulSoup(driver.page_source, 'lxml')

    # get the table
    table = soup.select("table")
    # convert the table data into a data that will be used in the dataframe with Pandas
    df = pd.read_html(str(table), header=0)
    # append data to data list
    datalist.append(df[0])

    driver.execute_script("window.history.go(-1)")

driver.quit()

df_result = pd.concat([pd.DataFrame(datalist[i])
                       for i in range(len(datalist))], keys=query)

# add unamed column to the service column for readability
df_result['Service'] = df_result['Service'].fillna(
    '') + df_result['Unnamed: 0'].fillna('')

print(df_result)
