# Columns to be filled
columns_to_fill = ["Founders", "Year Founded", "Website", "Status"]

# Add data to row


def access_afya_data(frame):
    frame.loc["Access Afya", columns_to_fill] = [
        "Melissa Menke",
        2012,
        "https://www.accessafya.com",
        "Operational",
    ]
