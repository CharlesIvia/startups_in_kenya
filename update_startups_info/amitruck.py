# Columns to be filled
columns_to_fill = ["Founders", "Year Founded", "Website", "Status"]

# Add data to row
def amitruck_data(frame):
    frame.loc["Amitruck", columns_to_fill] = [
        "Mark Mwangi",
        2016,
        "https://www.amitruck.com/",
        "Operational",
    ]
