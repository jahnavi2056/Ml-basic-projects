import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load data from CSV
df = pd.read_csv("C:\\Users\\DELL\\OneDrive\\Desktop\\HousePricePrediction\\manual_house_prices.csv")

# Step 2: Mean, Median, Mode
mean_price = df['Price (INR)'].mean()
median_price = df['Price (INR)'].median()
mode_price = df['Price (INR)'].mode()[0]

print("===== Central Tendency =====")
print(f"Mean Price   : ₹{mean_price:,.0f}")
print(f"Median Price : ₹{median_price:,.0f}")
print(f"Mode Price   : ₹{mode_price:,.0f}")

# Step 3: Histogram
plt.figure(figsize=(10, 5))
sns.histplot(df['Price (INR)'], bins=10, kde=True)
plt.title('House Price Distribution')
plt.xlabel('Price (INR)')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig("manual_price_histogram.png")
plt.show()

# Step 4: Boxplot
plt.figure(figsize=(8, 2))
sns.boxplot(x=df['Price (INR)'])
plt.title('Boxplot of House Prices')
plt.tight_layout()
plt.savefig("manual_price_boxplot.png")
plt.show()

# Step 5: Outlier Analysis
print("\n===== Descriptive Stats =====")
print(df['Price (INR)'].describe())

diff = mean_price - median_price
skew = df['Price (INR)'].skew()

print(f"\nMean is ₹{diff:,.0f} more than Median → Outlier Impact!")
print(f"Skewness of data: {skew:.2f} (Right skew if > 0)")

if skew > 1:
    msg = "Highly right-skewed"
elif skew > 0.5:
    msg = "Moderately right-skewed"
else:
    msg = "Fairly symmetrical"

print("\n===== Conclusion =====")
print(f"The data is {msg}.")
print("Mean is pulled upward by two very expensive houses (outliers).")
print("Median is more representative of typical house prices.")
