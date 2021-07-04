# Columns to be filled
columns_to_fill = ["Founders", "Year Founded", "Website", "Status"]

# Add data to row
def africa_sokoni_data(frame):
    frame.loc["AfricaSokoni", columns_to_fill] = [
        " Ebrima Fatty",
        2017,
        "https://africasokoni.co.ke/",
        "Operational",
    ]
