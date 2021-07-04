# Columns to be filled
columns_to_fill = ["Founders", "Year Founded", "Website", "Status"]

# Add data to row


def africas_talking_data(frame):
    frame.loc["Africa's Talking", columns_to_fill] = [
        "Eston Kimani, Samuel Gikandi",
        2010,
        "https://africastalking.com",
        "Operational",
    ]
