# Columns to be filled
columns_to_fill = ["Founders", "Year Founded", "Website", "Status"]

# Add data to row
def alternative_circle_data(frame):
    frame.loc["Alternative Circle", columns_to_fill] = [
        "Kevin Mutiso, Antony Magayu Kariuki",
        2016,
        "https://www.alternativecircle.com/",
        "Operational",
    ]
