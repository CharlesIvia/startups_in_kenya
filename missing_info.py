# Required libraries
import pandas as pd
from update_startups_info import access_afya, afribon

# Read-in Data
df = pd.read_csv("./data/startups.csv", index_col="Startup")
# Drop unwanted column
df = df.drop("Unnamed: 0", axis=1)

# Create additional columns
df[["Founders", "Year Founded", "Website", "Status"]] = None
print(df)
print(df.columns)

# Access Afya
access_afya.access_afya_data(df)
print(df)

# Afribon
afribon.afribon_data(df)
print(df)

# Save dataframe

df.to_csv("./data/main.csv")
