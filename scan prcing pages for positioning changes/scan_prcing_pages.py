import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns

# --- Fetch Competitor Pricing Page ---
def fetch_pricing_page(url):
    print(f"Fetching pricing page from {url}...")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Adjust this according to the structure of the competitor's page
    pricing_info = []
    products = soup.find_all('div', class_='pricing-product')  # Example class, change as needed

    for product in products:
        name = product.find('span', class_='product-name').text.strip()  # Change selector based on HTML structure
        price = product.find('span', class_='price').text.strip()  # Example price selector
        pricing_info.append((name, price))
    
    return pricing_info

# --- Track Pricing Changes ---
def track_pricing_changes(pricing_info, previous_data):
    # Convert price strings to numbers for comparison (handle currency symbols)
    cleaned_pricing_info = {item[0]: float(item[1].replace('$', '').replace(',', '').strip()) for item in pricing_info}
    
    if previous_data:
        changes = []
        for product, price in cleaned_pricing_info.items():
            if product in previous_data:
                previous_price = previous_data[product]
                if price != previous_price:
                    changes.append((product, previous_price, price))
        return changes, cleaned_pricing_info
    else:
        return [], cleaned_pricing_info

# --- Store and Visualize Data ---
def store_and_visualize_changes(data, filename="pricing_changes.csv"):
    df = pd.DataFrame(data, columns=["Product", "Old Price", "New Price", "Timestamp"])
    df.to_csv(filename, mode='a', header=False, index=False)
    
    # Plotting the data (example using product prices over time)
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x="Timestamp", y="New Price", hue="Product")
    plt.title("Pricing Changes Over Time")
    plt.show()

# --- Main Function ---
def main():
    competitor_url = "https://www.competitorwebsite.com/pricing"  # Replace with competitor's pricing page URL
    previous_data = None
    data_store = []
    
    while True:
        print("Scanning pricing page...")
        pricing_info = fetch_pricing_page(competitor_url)
        changes, updated_data = track_pricing_changes(pricing_info, previous_data)
        
        if changes:
            print("Detected pricing changes:")
            for product, old_price, new_price in changes:
                print(f"{product}: {old_price} -> {new_price}")
                timestamp = pd.Timestamp.now()
                for product, old_price, new_price in changes:
                    data_store.append([product, old_price, new_price, timestamp])
            
            # Store and visualize changes
            store_and_visualize_changes(data_store)
        
        # Update previous data for next iteration
        previous_data = updated_data
        
        # Wait for the next scan (for example, wait for 24 hours)
        print("Waiting for next scan...")
        time.sleep(86400)  # Sleep for 1 day (24 hours)

if __name__ == "__main__":
    main()
