# Columns to be filled
columns_to_fill = ["Founders", "Year Founded", "Website", "Status"]

# Add data to row
def asilimia_data(frame):
    frame.loc["Asilimia", columns_to_fill] = [
        "Maxime Servettaz, Tekwane Mwendwa",
        2017,
        "https://asilimia.co.ke/home",
        "Operational",
    ]
