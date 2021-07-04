# Columns to be filled
columns_to_fill = ["Founders", "Year Founded", "Website", "Status"]

# Add data to row
def ajua_data(frame):
    frame.loc["Ajua", columns_to_fill] = [
        "Kenfield Griffith, Louis Majanja",
        2012,
        "https://ajua.com/",
        "Operational",
    ]
