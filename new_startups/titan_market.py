# Import required libraries
import pandas as pd

# A list of keys
columns = [
    "Startup",
    "Overview",
    "Industries",
    "Last Round",
    "Total raised",
    "Founders",
    "Year Founded",
    "Website",
    "Status",
]

# Create values for the above keys
values = [
    "Titan Market",
    "Titan Market enables SMEs to create customizable online stores easily",
    "SMEs, eCommerce",
    "NaN",
    "NaN",
    "Charles Ivia",
    2018,
    "https://titanmarket.co.ke",
    "Alive",
]

# Create row
def new_titan_market(frame):
    new_row = dict(zip(columns, values))
    frame = frame.append(new_row, ignore_index=True)
    return frame
