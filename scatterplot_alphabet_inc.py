import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv("C:/Users/HP/Downloads/GOOG.csv")

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

start_date = '2023-02-20'
end_date = '2024-02-20'

# Filter the DataFrame to include only the rows between the two specific dates
filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

# Create a scatter plot of trading volume/stock prices
plt.figure(figsize=(10, 6))
plt.scatter(filtered_df['Date'], filtered_df['Volume'], c=filtered_df['Close'], cmap='viridis', alpha=0.5)
plt.title('Trading Volume/Stock Prices of Alphabet Inc.')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.colorbar(label='Close Price ($)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
