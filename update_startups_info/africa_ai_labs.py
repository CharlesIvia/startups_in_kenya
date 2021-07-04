# Columns to be filled
columns_to_fill = ["Founders", "Year Founded", "Website", "Status"]

# Add data to row


def africa_ai_labs_data(frame):
    frame.loc["Africa AI Labs", columns_to_fill] = [
        "Vassia Daskalakis",
        2020,
        "https://www.africai.co/",
        "Operational",
    ]
