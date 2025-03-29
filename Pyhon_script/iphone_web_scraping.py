# #  on 27_03-2025 i removed 'Apple iPhone 14 Pro (256 GB) - Deep Purple (Renewed)' from the filtered list 
# #       because there was no price listed in the website therefor list item was mismatched

# from bs4 import BeautifulSoup
# import requests
# url = 'https://www.amazon.ae/s?k=iphone&crid=3Q3DZ0PUU1PWJ&sprefix=%2Caps%2C196&ref=nb_sb_ss_recent_1_0_recent'
# page = requests.get(url)
# soup = BeautifulSoup(page.text,'html')
# all_listitems = soup.find('div', class_= "s-main-slot s-result-list s-search-results sg-row")
# name = all_listitems.find_all('h2')
# clear_name = [_.text for _ in name]
# filtered_list = [item for item in clear_name if item not in ['Results', 'More results','Related searches']]
    
# # print(filtered_list)
# # print(len(filtered_list))




# #for price
# price = all_listitems.find_all('span', class_ = 'a-price-whole')
# clean_price = [_.text for _ in price]
# # print(clean_price)
# # print(len(clean_price))


# import pandas as pd
# from datetime import datetime

# df = pd.DataFrame({'Product Name': filtered_list, 'Price': clean_price, 'date':datetime.today()})
# print(df)
# # today
# today_date = str(datetime.today().strftime('%Y-%m-%d'))
# df.to_csv(rf'C:\my_work\IPhone_Price_Everyday\CSV_files\Price_on_{today_date}.csv')
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
        df = pd.DataFrame({'Product Name': filtered_names, 'Price': prices, 'Date': datetime.today().strftime('%Y-%m-%d')})
        print(df)
        # Save as CSV
        # folder_path = r'C:\my_work\IPhone_Price_Everyday\CSV_files'
        # os.makedirs(folder_path, exist_ok=True)  # Ensure directory exists
        # today_date = datetime.today().strftime('%Y-%m-%d')
        # file_path = os.path.join(folder_path, f'Price_on_{today_date}.csv')

        # df.to_csv(file_path, index=False, encoding='utf-8')

        print("✅ Data scraped and saved successfully!")
    else:
        print("⚠️ Could not find the product list on the page.")
else:
    print(f"❌ Failed to fetch the webpage. Status Code: {page.status_code}")
