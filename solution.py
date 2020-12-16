from selenium import webdriver
import bs4
import pandas as pd
import os


def search_for_countries(url, query):
    '''
        Runs selenium using firefox webdriver.
        Loops through the query list above.
        Gets the page source and uses beautiful soup to get the tables on each page.
        Uses pandas to read the html and create a df form the data.
        Store the data in the datalist variable.
        Quit once looped through all vaiables.
    '''

    datalist = []

    # create a new Firefox session
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.get(url)

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

    return datalist


query = ["Brazil.", "South Africa.", "Portugal.",
         "Chile.", "Iceland.", "China.", "Madagascar."]

url = "http://www.three.co.uk/Support/Roaming_and_international/Roaming_Abroad/Destinations?#countries2"

datalist = search_for_countries(url, query)

# gets the datalist list and concats to a pandas dataframe
df_result = pd.concat([pd.DataFrame(datalist[i])
                       for i in range(len(datalist))], keys=query)

# removes all the NaN values
df_result = df_result.fillna('')

# add unamed column to the service column for readability
df_result['Service'] = df_result['Service'] + df_result['Unnamed: 0']

# removed the unamed column
df_result = df_result.drop(['Unnamed: 0'], axis=1)

path = os.getcwd()

# convert to csv file
df_result.to_csv(path + '/phone_costs.csv', index=True, encoding='utf-8')
