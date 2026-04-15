import pandas as pd

data = {
    "Product": ["Apple", "Banana", "Orange", "Apple", "Banana", "Orange"],
    "Sales": [10, 20, 15, 25, 30, 5],
    "Price": [2.5, 1.2, 1.8, 2.5, 1.2, 1.8],
    "Date": [
        "2026-04-10", "2026-04-10", "2026-04-10",
        "2026-04-11", "2026-04-11", "2026-04-11"
    ]
}

df = pd.DataFrame(data)
df.to_excel("sales_data.xlsx", index=False)

print("sales_data.xlsx created!")