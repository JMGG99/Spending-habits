import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('spending_patterns_detailed.csv')  # Replace with the actual dataset file name

# Plot a histogram to visualize the spending distribution
plt.figure(figsize=(8, 6))
sns.histplot(df['Total Spent'], bins=20, kde=True, color='skyblue')  # kde=True adds a density curve
plt.title('Total Spending Distribution', fontsize=14)
plt.xlabel('Total Spent', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.show()


# Create a bar plot to compare the spending by Payment Method
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x='Payment Method', y='Total Spent', ci=None, palette='viridis')
plt.title('Total Spending by Payment Method', fontsize=14)
plt.xlabel('Payment Method', fontsize=12)
plt.ylabel('Total Spending', fontsize=12)
plt.show()


# Scatter plot showing the relationship between Quantity and Price Per Unit
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Quantity', y='Price Per Unit', hue='Category', alpha=0.7)
plt.title('Relationship Between Quantity and Price Per Unit', fontsize=14)
plt.xlabel('Quantity', fontsize=12)
plt.ylabel('Price Per Unit', fontsize=12)
plt.show()

# Sum total spending by Category
category_spending = df.groupby('Category')['Total Spent'].sum().reset_index()

# Create a bar plot for total spending by category
plt.figure(figsize=(10, 6))
sns.barplot(data=category_spending, x='Total Spent', y='Category', palette='coolwarm', ci=None)
plt.title('Total Spending by Category', fontsize=14)
plt.xlabel('Total Spending', fontsize=12)
plt.ylabel('Category', fontsize=12)
plt.show()

# Convert the 'Transaction Date' column to datetime
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])

# Extract month and year from the transaction date
df['Month-Year'] = df['Transaction Date'].dt.to_period('M')

# Count the number of transactions per month-year
transaction_count = df['Month-Year'].value_counts().reset_index()
transaction_count.columns = ['Month-Year', 'Transaction Count']

# Create a bar plot to show the frequency of transactions by month
plt.figure(figsize=(10, 6))
sns.barplot(data=transaction_count, x='Month-Year', y='Transaction Count', palette='muted')
plt.title('Transaction Frequency by Month-Year', fontsize=14)
plt.xlabel('Month-Year', fontsize=12)
plt.ylabel('Transaction Count', fontsize=12)
plt.xticks(rotation=45)
plt.show()