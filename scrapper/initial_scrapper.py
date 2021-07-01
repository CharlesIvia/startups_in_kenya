# This script Kenyan scraps startups from startupranking.com

# Import required libraries

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen

# URLs

first_page = "https://www.startupranking.com/top/kenya"
second_page = "https://www.startupranking.com/top/kenya/2"
third_page = "https://www.startupranking.com/top/kenya/3"

# Function to read data from


def read_data(url):
    """Disguise our request by sending a HTTP header indicating the request was being sent from the Firefox web browser"""
    req = Request(url, headers={"User-agent": "Mozilla/5.0"})
    webpage = urlopen(req).read()
    tables = pd.read_html(webpage)
    """Check number of tables"""
    print(len(tables))
    return tables


# Call the function and create dataframes

first_df = read_data(first_page)[0]
second_df = read_data(second_page)[0]
third_df = read_data(third_page)[0]

dataframes = [first_df, second_df, third_df]

# Combine dataframes into a single dataframe

df = pd.concat(dataframes, axis=0, ignore_index=True)

print(f"Cobined dataframe {df}")

# Initial data cleaning
# From the above dataframe, we only need the Startup and Description columns

clean_df = df.drop(["Rank", "SR Score", "Country Rank"], axis=1)
print(clean_df)

#Save dataframe as csv 
clean_df.to_csv("initial_scrapper_data.csv")