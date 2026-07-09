# ==============================
# TASK 2: Exploratory Data Analysis (EDA)
# ==============================

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------
# Load Dataset
# ------------------------------
df = pd.read_csv("books.csv")

print("=" * 60)
print("BOOK DATASET")
print("=" * 60)

# ------------------------------
# 1. Ask Meaningful Questions
# ------------------------------
print("\n1. QUESTIONS BEFORE ANALYSIS")
print("-" * 60)

questions = [
    "1. How many books are available in the dataset?",
    "2. What is the average price of books?",
    "3. Which is the most expensive book?",
    "4. Which is the cheapest book?",
    "5. Are there any missing values?",
    "6. Are there any duplicate records?",
    "7. How are book prices distributed?",
    "8. Are there any outliers in book prices?"
]

for q in questions:
    print(q)

# ------------------------------
# 2. Explore Data Structure
# ------------------------------
print("\n2. DATA STRUCTURE")
print("-" * 60)

print("\nFirst 5 Rows")
print(df.head())

print("\nLast 5 Rows")
print(df.tail())

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

print("\nDataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

# ------------------------------
# 3. Identify Trends and Patterns
# ------------------------------
print("\n3. TRENDS AND PATTERNS")
print("-" * 60)

print("Total Books :", len(df))
print("Average Price :", round(df["Price"].mean(), 2))
print("Maximum Price :", df["Price"].max())
print("Minimum Price :", df["Price"].min())
print("Median Price :", df["Price"].median())
print("Standard Deviation :", round(df["Price"].std(), 2))

print("\nTop 10 Most Expensive Books")
print(df.sort_values(by="Price", ascending=False).head(10))

print("\nTop 10 Cheapest Books")
print(df.sort_values(by="Price").head(10))

# ------------------------------
# 4. Hypothesis Testing
# ------------------------------
print("\n4. HYPOTHESIS TESTING")
print("-" * 60)

print("\nHypothesis 1:")
print("Most books cost less than £50.")

books_under_50 = df[df["Price"] < 50]

print("Books under £50 :", len(books_under_50))
print("Percentage :", round((len(books_under_50)/len(df))*100,2), "%")

if len(books_under_50) > len(df)/2:
    print("Result : Hypothesis Supported")
else:
    print("Result : Hypothesis Not Supported")

print("\nHypothesis 2:")
print("Dataset contains no missing values.")

missing = df.isnull().sum()

print(missing)

if missing.sum()==0:
    print("Result : Supported")
else:
    print("Result : Not Supported")

print("\nHypothesis 3:")
print("Dataset contains no duplicate records.")

duplicates = df.duplicated().sum()

print("Duplicate Records :", duplicates)

if duplicates==0:
    print("Result : Supported")
else:
    print("Result : Not Supported")

# ------------------------------
# 5. Detect Data Issues
# ------------------------------
print("\n5. DATA QUALITY CHECK")
print("-" * 60)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Records")
print(df.duplicated().sum())

print("\nNegative Prices")
negative = df[df["Price"] < 0]

if len(negative)==0:
    print("No Negative Prices Found")
else:
    print(negative)

print("\nData Types")
print(df.dtypes)

# ------------------------------
# 6. Visualization
# ------------------------------

# Histogram
plt.figure(figsize=(8,5))
plt.hist(df["Price"], bins=20, edgecolor="black")
plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.grid(True)
plt.show()

# Box Plot
plt.figure(figsize=(5,6))
plt.boxplot(df["Price"])
plt.title("Book Price Box Plot")
plt.ylabel("Price (£)")
plt.grid(True)
plt.show()

# Bar Chart - Top 10 Expensive Books
top10 = df.sort_values(by="Price", ascending=False).head(10)

plt.figure(figsize=(12,6))
plt.bar(top10["Book Title"], top10["Price"])
plt.xticks(rotation=90)
plt.title("Top 10 Most Expensive Books")
plt.xlabel("Book Title")
plt.ylabel("Price (£)")
plt.tight_layout()
plt.show()

# ------------------------------
# 7. Final Conclusion
# ------------------------------
print("\n6. CONCLUSION")
print("-" * 60)

print(f"""
1. Total Books               : {len(df)}
2. Average Price             : {round(df['Price'].mean(),2)}
3. Highest Price             : {df['Price'].max()}
4. Lowest Price              : {df['Price'].min()}
5. Missing Values            : {df.isnull().sum().sum()}
6. Duplicate Records         : {df.duplicated().sum()}
7. Dataset is ready for further analysis if no missing or duplicate values exist.
""")
