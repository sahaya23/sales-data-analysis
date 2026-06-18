import pandas as pd
import matplotlib.pyplot as plt
import os

# ─────────────────────────────────────────
# STEP 1: LOAD DATA
# ─────────────────────────────────────────
df = pd.read_csv("sales_data.csv", encoding='latin1')

print("=" * 50)
print("SALES DATA ANALYSIS")
print("=" * 50)
print(f"\nTotal Rows: {df.shape[0]}, Total Columns: {df.shape[1]}")
print("\nFirst 5 Rows:")
print(df.head())
print("\nColumn Names:")
print(df.columns.tolist())
print("\nMissing Values:")
print(df.isnull().sum())

# ─────────────────────────────────────────
# STEP 2: CLEAN DATA
# ─────────────────────────────────────────
df.drop_duplicates(inplace=True)

# FIXED: date format for DD/MM/YYYY
df['Order Date'] = pd.to_datetime(df['Order Date'], format='mixed', dayfirst=True)
df['Ship Date']  = pd.to_datetime(df['Ship Date'],  format='mixed', dayfirst=True)

df['Month']      = df['Order Date'].dt.month
df['Year']       = df['Order Date'].dt.year
df['Month_Name'] = df['Order Date'].dt.strftime('%b')
df.dropna(subset=['Sales'], inplace=True)

print(f"\nAfter Cleaning — Rows remaining: {len(df)}")

# ─────────────────────────────────────────
# STEP 3: ANALYSIS
# ─────────────────────────────────────────

# Total overall sales & profit
total_sales  = df['Sales'].sum()
total_orders = df['Order ID'].nunique()

print("\n" + "=" * 50)
print("KEY METRICS")
print("=" * 50)
print(f"Total Sales   : ${total_sales:,.2f}")
print(f"Total Orders  : {total_orders}")

# Sales by Category
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print("\nSales by Category:")
print(category_sales)

# Sales by Sub-Category
subcategory_sales = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Sub-Categories by Sales:")
print(subcategory_sales)

# Monthly Sales Trend
monthly_sales = df.groupby('Month')['Sales'].sum()
print("\nMonthly Sales:")
print(monthly_sales)

# Top 5 States
top_states = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 States by Sales:")
print(top_states)

# Top 5 Products by Sales
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Products by Sales:")
print(top_products)

# Sales by Region
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print("\nSales by Region:")
print(region_sales)

# Sales by Segment
segment_sales = df.groupby('Segment')['Sales'].sum().sort_values(ascending=False)
print("\nSales by Segment:")
print(segment_sales)

# ─────────────────────────────────────────
# STEP 4: CHARTS
# ─────────────────────────────────────────
os.makedirs("charts", exist_ok=True)

# Chart 1: Sales by Category (Bar)
plt.figure(figsize=(8, 5))
category_sales.plot(kind='bar', color=['#4C72B0', '#55A868', '#C44E52'], edgecolor='black')
plt.title('Total Sales by Category', fontsize=14, fontweight='bold')
plt.xlabel('Category')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('charts/1_sales_by_category.png')
plt.show()
print("Chart 1 saved.")

# Chart 2: Monthly Sales Trend (Line)
plt.figure(figsize=(10, 5))
monthly_sales.plot(kind='line', marker='o', color='royalblue', linewidth=2)
plt.title('Monthly Sales Trend', fontsize=14, fontweight='bold')
plt.xlabel('Month (1=Jan ... 12=Dec)')
plt.ylabel('Total Sales ($)')
plt.xticks(range(1, 13))
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('charts/2_monthly_trend.png')
plt.show()
print("Chart 2 saved.")

# Chart 3: Top 5 States (Horizontal Bar)
plt.figure(figsize=(9, 5))
top_states.plot(kind='barh', color='seagreen', edgecolor='black')
plt.title('Top 5 States by Sales', fontsize=14, fontweight='bold')
plt.xlabel('Total Sales ($)')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('charts/3_top_states.png')
plt.show()
print("Chart 3 saved.")

# Chart 4: Sales Share by Category (Pie)
plt.figure(figsize=(6, 6))
category_sales.plot(kind='pie', autopct='%1.1f%%', startangle=90,
                    colors=['#4C72B0', '#55A868', '#C44E52'])
plt.title('Sales Share by Category', fontsize=14, fontweight='bold')
plt.ylabel('')
plt.tight_layout()
plt.savefig('charts/4_category_pie.png')
plt.show()
print("Chart 4 saved.")

# Chart 5: Top 10 Sub-Categories (Bar)
plt.figure(figsize=(10, 6))
subcategory_sales.plot(kind='bar', color='steelblue', edgecolor='black')
plt.title('Top 10 Sub-Categories by Sales', fontsize=14, fontweight='bold')
plt.xlabel('Sub-Category')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('charts/5_subcategory_sales.png')
plt.show()
print("Chart 5 saved.")

# Chart 6: Sales by Region (Bar)
plt.figure(figsize=(7, 5))
region_sales.plot(kind='bar', color=['#e07b54', '#5b8db8', '#7bbf72', '#f0c05a'], edgecolor='black')
plt.title('Sales by Region', fontsize=14, fontweight='bold')
plt.xlabel('Region')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('charts/6_sales_by_region.png')
plt.show()
print("Chart 6 saved.")

# Chart 7: Sales by Segment (Bar)
plt.figure(figsize=(7, 5))
segment_sales.plot(kind='bar', color=['#9b59b6', '#3498db', '#2ecc71'], edgecolor='black')
plt.title('Sales by Customer Segment', fontsize=14, fontweight='bold')
plt.xlabel('Segment')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('charts/7_sales_by_segment.png')
plt.show()
print("Chart 7 saved.")

# ─────────────────────────────────────────
# DONE
# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("ALL ANALYSIS COMPLETE!")
print("7 charts saved in the /charts folder.")
print("=" * 50)