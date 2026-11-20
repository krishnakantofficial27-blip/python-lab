import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Read CSV file using pandas
data_file = Path(__file__).resolve().with_name("sales.csv")
df = pd.read_csv(data_file, parse_dates=["Date"])
df = df.sort_values("Date")

# 1. Line Graph: Daily Sales Trend
pivot_df = df.pivot(index="Date", columns="Product", values="Sales")
for product in pivot_df.columns:
    plt.plot(pivot_df.index, pivot_df[product], marker="o", label=product)
plt.title("Daily Retail Sales Trend")
plt.legend()
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# 2. Bar Chart: Total Sales by Product
plt.figure()
total_sales = df.groupby("Product")["Sales"].sum()
plt.bar(total_sales.index, total_sales.values,
        color=["orange", "skyblue"][:len(total_sales)])
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.show()