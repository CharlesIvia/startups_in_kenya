# Required libraries
import pandas as pd
from new_startups import titan_market

# Read-in Data
df = pd.read_csv("./data/main.csv")
print(df)
print(df.columns)

# Titan Market
df = titan_market.new_titan_market(df)
print(df)

# Save as new_main.csv
df.to_csv("./data/new_main.csv")
