# Required libraries
import pandas as pd
from update_startups_info import (
    access_afya,
    afribon,
    africa_ai_labs,
    africas_talking,
    africa_sokoni,
    ajua,
    alternative_circle,
    amitruck,
    angaza,
    apollo_agriculture,
    asilimia,
    asoko_insight,
    aza_finance,
)

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

# Africa AI Labs
africa_ai_labs.africa_ai_labs_data(df)
print(df)

# Africa's Talking
africas_talking.africas_talking_data(df)
print(df)

# Africa Sokoni
africa_sokoni.africa_sokoni_data(df)
print(df)

# Ajua
ajua.ajua_data(df)
print(df.head(20))

# Alternative circle
alternative_circle.alternative_circle_data(df)
print(df.head(20))

# Amitruck
amitruck.amitruck_data(df)
print(df.head(20))

# Angaza
angaza.angaza_data(df)
print(df.head(20))

# Apollo agricluture
apollo_agriculture.apollo_agriculture_data(df)
print(df.head(20))

# Asimilia
asilimia.asilimia_data(df)

# Asoko Insight
asoko_insight.asoko_insight_data(df)

# Aza Finance
aza_finance.aza_finance_data(df)
print(df.head(20))

# Save dataframe
df.to_csv("./data/main.csv")
