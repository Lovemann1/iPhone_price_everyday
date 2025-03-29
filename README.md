# **iPhone Price Tracker on Amazon** 📊

This project tracks and compares iPhone prices on Amazon daily, extracting key details such as price, storage type, condition (new or renewed), and name. The data is processed using Python and Power BI for visualization.

## **Project Workflow** 🚀

1. **Web Scraping with Python** 🐍  
   - Scrapes iPhone prices from Amazon (iPhone XR to iPhone 16 Pro Max).  
   - Extracts key details:
     - Price 💰  
     - Storage Type 💾  
     - Condition (New/Renewed) 🔄  
     - Model Name 📱  
   - Runs daily to track price changes.  

2. **Data Processing with Pandas** 📝  
   - Stores extracted data in a **Pandas DataFrame**.  
   - Adds a **date column** to track daily price changes.  
   - Cleans and formats the data.  
   - Saves the cleaned data as a **CSV file** (one per day).  

3. **Power BI for Data Analysis** 📊  
   - Uses **Power Query** to extract, clean, filter, and shape data.  
   - Loads the cleaned dataset into **Power BI Dashboard**.  
   - Utilizes **DAX** for advanced visualizations.  

## **How It Works** 🔧  
- The Python script runs daily and generates a new CSV file with the latest iPhone prices.  
- Power BI automatically updates with new data, providing insights into price trends.  

## **Tech Stack** 🛠  
- **Python** (BeautifulSoup, Requests, Pandas)  
- **Power BI** (Power Query, DAX)  

## **Future Improvements** 🔮  
- Automate Power BI refresh.  
- Expand to other e-commerce platforms.  
- Add notifications for significant price drops.  

## **Setup & Usage** 🏗  

### **Prerequisites**  
- Python installed (3.x)  
- Required libraries:  
  ```bash
  pip install requests beautifulsoup4 pandas
  ```  
- Power BI installed  

### **Running the Script**  
``` Python
from bs4 import BeautifulSoup
import requests
url = 'https://www.amazon.ae/s?k=iphone&crid=3Q3DZ0PUU1PWJ&sprefix=%2Caps%2C196&ref=nb_sb_ss_recent_1_0_recent'
page = requests.get(url)
soup = BeautifulSoup(page.text,'html')
all_listitems = soup.find('div', class_= "s-main-slot s-result-list s-search-results sg-row")
name = all_listitems.find_all('h2')
clear_name = [_.text for _ in name]
filtered_list = [item for item in clear_name if item not in ['Results', 'More results','Related searches']]
    
# print(filtered_list)
# print(len(filtered_list))




#for price
price = all_listitems.find_all('span', class_ = 'a-price-whole')
clean_price = [_.text for _ in price]
# print(clean_price)
# print(len(clean_price))


import pandas as pd
from datetime import datetime

df = pd.DataFrame({'Product Name': filtered_list, 'Price': clean_price, 'date':datetime.today()})
print(df)
# today
today_date = str(datetime.today().strftime('%Y-%m-%d'))
df.to_csv(rf'C:\my_work\IPhone_Price_Everyday\CSV_files\Price_on_{today_date}.csv')
```
## **Power BI Dashboard & Visualizations** 📈

The Power BI dashboard includes the following visualizations:

![Power BI Interface](https://github.com/user-attachments/assets/755178fd-801c-4caf-b262-950e407c7c1f)


- **Line Graph for Price Trends** 📊  
  - Displays a **line graph for each iPhone series** (iPhone X to iPhone 16).  
  - Shows **price changes over time** to track trends.

- **Price Comparison Table** 📋  
  - Compares **today’s price** to the **lowest and highest recorded prices**.  
  - Helps identify the best time to buy.

- **Filters for Better Insights** 🔍  
  - **Storage Type:** Filter by different storage options (e.g., 128GB, 256GB, etc.).  
  - **Condition:** Filter between **New** and **Renewed** iPhones.

## **📌 Conclusion** 🚀  

This project provides a **comprehensive solution** for tracking **iPhone prices on Amazon** over time. By leveraging **Python for web scraping**, **Pandas for data processing**, and **Power BI for visualization**, it offers **real-time insights** into price fluctuations.  

With features like **historical price trends**, **daily price comparisons**, this dashboard helps users make **informed purchasing decisions**.  

Moving forward, future improvements such as **automating Power BI refresh, expanding to other e-commerce platforms, and adding price drop alerts** will enhance the system further.  

📊 **Whether you're a data enthusiast or a smart shopper, this project provides valuable insights into iPhone pricing trends!**

