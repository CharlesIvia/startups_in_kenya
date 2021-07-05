# Columns to be filled
columns_to_fill = ["Founders", "Year Founded", "Website", "Status"]

# Add data to row
def aza_finance_data(frame):
    frame.loc["Aza Finance", columns_to_fill] = [
        "Amy Ludlum, Charlene Chen, Elizabeth Rossiello",
        2013,
        "https://www.azafinance.com/",
        "Operational",
    ]
