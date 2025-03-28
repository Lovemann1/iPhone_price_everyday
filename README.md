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
```bash
python scrape_iphone_prices.py
