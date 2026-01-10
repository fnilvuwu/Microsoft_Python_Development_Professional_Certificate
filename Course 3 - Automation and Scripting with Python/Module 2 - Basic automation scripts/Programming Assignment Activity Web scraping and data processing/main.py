import requests
import pandas as pd
from bs4 import BeautifulSoup

# URL of your local HTML file (served by Live Server or similar)
url = "http://127.0.0.1:5500/baseball_stats.html"

# Step 1: Fetch the webpage content
response = requests.get(url)
response.raise_for_status()  # Check for request errors

# Step 2: Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# (Optional) Inspect the HTML
# print(soup.prettify())

# Step 3: Extract the table using pandas
# This automatically finds all <table> tags and converts them to DataFrames
tables = pd.read_html(response.text)

# There is only one table in your HTML, so take the first one
baseball_df = tables[0]

# Step 4: Inspect the DataFrame
print("First 5 rows:")
print(baseball_df.head())
print("\nDataFrame Info:")
print(baseball_df.info())
print("\nShape of DataFrame:", baseball_df.shape)

# Step 5: Save to CSV
output_file = "sports_statistics.csv"
baseball_df.to_csv(output_file, index=False)

print(f"\nData successfully saved to {output_file}")
