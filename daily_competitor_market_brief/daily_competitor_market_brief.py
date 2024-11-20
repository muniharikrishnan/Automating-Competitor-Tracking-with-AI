import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import time

# --- Function to Fetch Competitor Pricing Data ---
def fetch_pricing_data(url):
    print("Fetching competitor pricing data...")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract relevant product pricing information
    products = []
    pricing_elements = soup.find_all('div', class_='pricing-class')  # Update with real class
    for element in pricing_elements:
        product_name = element.find('span', class_='product-name').text
        price = element.find('span', class_='product-price').text
        products.append((product_name, price))

    return products

# --- Function to Analyze App Reviews ---
def analyze_reviews(app_id):
    print("Fetching and analyzing reviews...")
    url = f"https://play.google.com/store/apps/details?id={app_id}&showAllReviews=true"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    reviews = [review.text.strip() for review in soup.find_all('div', class_='UD7Dzf')][:100]
    sentiment = {'positive': [], 'neutral': [], 'negative': []}
    
    for review in reviews:
        analysis = TextBlob(review).sentiment
        if analysis.polarity > 0.1:
            sentiment['positive'].append(review)
        elif analysis.polarity < -0.1:
            sentiment['negative'].append(review)
        else:
            sentiment['neutral'].append(review)

    return sentiment

# --- Function to Create Daily Brief ---
def create_daily_brief():
    print("Creating daily brief...")

    # Competitor Data
    competitor_url = "https://example.com/competitor-pricing-page"  # Replace with actual URL
    pricing_data = fetch_pricing_data(competitor_url)
    
    # App Review Sentiment Analysis
    app_id = "com.example.app"  # Replace with actual app ID
    review_sentiments = analyze_reviews(app_id)

    # Format the daily brief
    brief = f"Daily Competitor & Market Brief - {datetime.date.today()}\n\n"
    
    brief += "=== Competitor Pricing Changes ===\n"
    for product, price in pricing_data:
        brief += f"Product: {product}, Price: {price}\n"
    
    brief += "\n=== App Reviews Sentiment Analysis ===\n"
    brief += f"Positive Reviews: {len(review_sentiments['positive'])}\n"
    brief += f"Neutral Reviews: {len(review_sentiments['neutral'])}\n"
    brief += f"Negative Reviews: {len(review_sentiments['negative'])}\n"
    
    brief += "\n=== Top Negative Review Insights ===\n"
    brief += "\n".join(review_sentiments['negative'][:5])  # Display top 5 negative reviews

    return brief

# --- Function to Send Daily Brief via Email ---
def send_daily_brief(brief, recipient_email):
    print("Sending daily brief via email...")

    sender_email = "your_email@example.com"
    password = "your_email_password"
    
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "Daily Competitor & Market Brief"
    
    # Attach the body text
    msg.attach(MIMEText(brief, 'plain'))

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, recipient_email, text)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

# --- Main Function to Automate the Process ---
def main():
    recipient_email = "stakeholder@example.com"  # Replace with the recipient's email
    while True:
        daily_brief = create_daily_brief()
        send_daily_brief(daily_brief, recipient_email)
        
        # Wait for the next day (86400 seconds = 24 hours)
        time.sleep(86400)

if __name__ == "__main__":
    main()
