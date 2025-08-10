import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mode, median, mean

# Load the dataset
df = pd.read_csv("C:\\Users\\DELL\\OneDrive\\Desktop\\HousePricePrediction\\products_rating.csv")

# Compute statistics
ratings = df["Rating"]
mean_rating = mean(ratings)
median_rating = median(ratings)
mode_rating = mode(ratings)

print("=== Feedback Rating Analysis ===")
print(f"Mean Rating: {mean_rating:.2f}")
print(f"Median Rating: {median_rating}")
print(f"Mode Rating: {mode_rating}")

# Plot Histogram
plt.figure(figsize=(8, 5))
sns.histplot(ratings, bins=5, kde=False)
plt.title("Distribution of Customer Ratings")
plt.xlabel("Rating (1-5)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Plot Boxplot
plt.figure(figsize=(6, 4))
sns.boxplot(x=ratings)
plt.title("Boxplot of Customer Ratings")
plt.xlabel("Rating")
plt.grid(True)
plt.show()
