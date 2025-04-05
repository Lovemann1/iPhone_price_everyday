
from bs4 import BeautifulSoup
import requests

url = 'https://www.amazon.ae/s?k=iphone&crid=3Q3DZ0PUU1PWJ&sprefix=%2Caps%2C196&ref=nb_sb_ss_recent_1_0_recent'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')

all_listitems = soup.find_all('div', role="listitem")

clean_name = []
clean_price = []

for item in all_listitems:
    name_tag = item.find("h2")
    price_tag = item.find("span", class_="a-price-whole")
    
    if name_tag and price_tag:
        name = name_tag.text.strip()
        clean_name.append(name)
        
        price = price_tag.text.strip().replace(',', '')
        clean_price.append(price)
# print(clean_name)
# print(len(clean_name))
# print(len(clean_price))
# print(clean_price)



import pandas as pd
from datetime import datetime

df = pd.DataFrame({'Product Name': clean_name, 'Price': clean_price, 'date':datetime.today()})
print(df)

# today
today_date = str(datetime.today().strftime('%Y-%m-%d'))
# save data to csv file
df.to_csv(rf'C:\my_work\IPhone_Price_Everyday\CSV_files\Price_on_{today_date}.csv')
