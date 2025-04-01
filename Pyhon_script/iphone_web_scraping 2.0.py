
# this code was giving me total 52 products while my code was giving me 48 products 
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os

# Define URL
url = 'https://www.amazon.ae/s?k=iphone&crid=3Q3DZ0PUU1PWJ&sprefix=%2Caps%2C196&ref=nb_sb_ss_recent_1_0_recent'

# Headers to avoid request blocking
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Get page content
page = requests.get(url, headers=headers)

# Check if the request was successful
if page.status_code == 200:
    soup = BeautifulSoup(page.text, 'html.parser')

    # Extract product names
    all_listitems = soup.find('div', class_="s-main-slot s-result-list s-search-results sg-row")
    if all_listitems:
        name_tags = all_listitems.find_all('h2')
        product_names = [name.get_text(strip=True) for name in name_tags]

        # Remove irrelevant items
        filtered_names = [name for name in product_names if name.lower() not in ['results', 'more results', 'related searches']]

        # Extract prices
        price_tags = all_listitems.find_all('span', class_='a-price-whole')
        prices = [price.get_text(strip=True).replace(',', '') for price in price_tags]  # Remove commas from numbers

        # Ensure lists are the same length
        min_length = min(len(filtered_names), len(prices))
        filtered_names = filtered_names[:min_length]
        prices = prices[:min_length]

        # Create DataFrame
        df = pd.DataFrame({'Product Name': filtered_names, 'Price': prices, 'date': datetime.today()})
        print(df)
        #Save as CSV
        folder_path = r'C:\my_work\IPhone_Price_Everyday\CSV_files'
        os.makedirs(folder_path, exist_ok=True)  # Ensure directory exists
        today_date = datetime.today().strftime('%Y-%m-%d')
        file_path = os.path.join(folder_path, f'Price_on_{today_date}.csv')

        df.to_csv(file_path, encoding='utf-8')

        print("✅ Data scraped and saved successfully!")
    else:
        print("⚠️ Could not find the product list on the page.")
else:
    print(f"❌ Failed to fetch the webpage. Status Code: {page.status_code}")
