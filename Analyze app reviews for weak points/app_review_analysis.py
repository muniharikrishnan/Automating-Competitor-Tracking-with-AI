import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# --- Fetch App Reviews (Google Play Store Example) ---
def fetch_reviews(app_id, num_reviews=100):
    print(f"Fetching reviews for App ID: {app_id}...")
    reviews = []
    url = f"https://play.google.com/store/apps/details?id={app_id}&showAllReviews=true"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    review_elements = soup.find_all('div', class_='UD7Dzf')[:num_reviews]
    for review in review_elements:
        reviews.append(review.text.strip())
    return reviews

# --- Perform Sentiment Analysis ---
def analyze_sentiment(reviews):
    print("Analyzing review sentiments...")
    sentiments = {'positive': [], 'neutral': [], 'negative': []}

    for review in reviews:
        analysis = TextBlob(review).sentiment
        if analysis.polarity > 0.1:
            sentiments['positive'].append(review)
        elif analysis.polarity < -0.1:
            sentiments['negative'].append(review)
        else:
            sentiments['neutral'].append(review)

    return sentiments

# --- Extract Weak Points ---
def extract_weak_points(reviews):
    print("Extracting weak points from negative reviews...")
    all_words = " ".join(reviews).lower().split()
    common_words = Counter(all_words).most_common(20)
    return common_words

# --- Visualize Weak Points ---
def visualize_weak_points(common_words):
    print("Visualizing weak points...")
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict(common_words))
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# --- Main Function ---
def analyse_review_and_sentiment():
    app_id = "com.automatingcompetitortrackingwithai"  # Use the project name as the app ID
    reviews = fetch_reviews(app_id)

    if reviews:
        sentiments = analyze_sentiment(reviews)
        print(f"Positive Reviews: {len(sentiments['positive'])}")
        print(f"Neutral Reviews: {len(sentiments['neutral'])}")
        print(f"Negative Reviews: {len(sentiments['negative'])}")

        weak_points = extract_weak_points(sentiments['negative'])
        print("Top Weak Points:", weak_points)

        visualize_weak_points(weak_points)
    else:
        print("No reviews found or unable to fetch reviews.")

if __name__ == "__main__":
    analyse_review_and_sentiment()