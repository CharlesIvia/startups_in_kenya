# Columns to be filled
columns_to_fill = ["Founders", "Year Founded", "Website", "Status"]

# Add data to row
def asoko_insight_data(frame):
    frame.loc["Asoko Insight", columns_to_fill] = [
        "Greg Cohen, Rob Withagen",
        2013,
        "http://asokoinsight.com/",
        "Operational",
    ]
