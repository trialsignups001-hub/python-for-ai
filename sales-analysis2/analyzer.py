import pandas as pd
from helpers import calculate_total, format_currency

df = pd.read_csv("data/sales.csv")
print(df)
totals = []

for index,row in df.iterrows():
    total = calculate_total (row["quantity"],row["price"])
    totals.append(total)

df["total"] = totals

print(df)

updated_currency = []

updated_total = []
for i in df["total"]:
   updated_total= format_currency(i)
   updated_currency.append(updated_total)

df["With Currency"] = updated_currency

grand_total = sum(df["total"])

print(f"grand_total:{grand_total}")


