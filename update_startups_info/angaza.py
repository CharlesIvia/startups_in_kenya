# Columns to be filled
columns_to_fill = ["Founders", "Year Founded", "Website", "Status"]

# Add data to row
def angaza_data(frame):
    frame.loc["Angaza", columns_to_fill] = [
        "Bryan Duggan, Bryan Silverthorn, Lesley Marincola, Victoria Arch",
        2016,
        "https://www.angaza.com/",
        "Operational",
    ]
