# Columns to be filled
columns_to_fill = ["Founders", "Year Founded", "Website", "Status"]

# Add data to row
def apollo_agriculture_data(frame):
    frame.loc["Apollo Agriculture", columns_to_fill] = [
        "Benjamin Njenga, Earl St Sauver, Eli Pollak",
        2015,
        "https://www.apolloagriculture.com/",
        "Operational",
    ]
