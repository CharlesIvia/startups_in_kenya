# This script scraps Kenyan startups from https://startuplist.africa/

# Import required libraries

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
from selenium import webdriver

# URLs

url = "https://startuplist.africa/startups-in-kenya"

# Driver path
driver_path = "C:\webdrivers\chromedriver.exe"

# Read Data
driver = webdriver.Chrome(driver_path)
driver.get(url=url)

# Wait for page content to load
driver.implicitly_wait(40)

# Get data from first page
html = driver.page_source
table = pd.read_html(html)
first_page = table[0]

# Create dataframe and append data from first page
data = pd.DataFrame()
data = data.append(first_page, ignore_index=True)

# nextbutton
next_button = driver.find_element_by_class_name("pagination-next")

# Loop through the remaining pages
for i in range(0, 12):
    next_button.click()
    html = driver.page_source
    table = pd.read_html(html)
    page_data = table[0]
    data = data.append(page_data, ignore_index=True)

df = data
print(df)

# Save data
df.to_csv("./data/startups.csv")
driver.close()
