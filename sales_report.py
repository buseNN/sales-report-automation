import pandas as pd
from datetime import datetime


df = pd.read_excel("sales_data.xlsx", engine="openpyxl")


total = df["Sales"].sum()
average = df["Sales"].mean()

report = df.groupby("Product")["Sales"].sum()

top_product = report.idxmax()
top_value = report.max()

worst_product = report.idxmin()
worst_value = report.min()


today = datetime.now().strftime("%Y-%m-%d")


summary = pd.DataFrame({
    "Metric": [
        "Date",
        "Total Sales",
        "Average Sales",
        "Top Product",
        "Worst Product"
    ],
    "Value": [
        today,
        total,
        round(average, 2),
        f"{top_product} ({top_value})",
        f"{worst_product} ({worst_value})"
    ]
})


summary.to_excel("daily_report.xlsx", index=False)

print("Report created successfully!")