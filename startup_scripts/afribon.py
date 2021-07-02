# Columns to be filled
columns_to_fill = ["Founders", "Year Founded", "Website", "Status"]

# Add data to row

def afribon_data(frame):
    frame.loc["Afribon", columns_to_fill] = [
        "Julian Giuge, Anne Merienne",
        2012,
        "https://www.afribon.com/",
        "Operational",
    ]
