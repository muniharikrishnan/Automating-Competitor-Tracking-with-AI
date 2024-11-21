# Automating-Competitor-Tracking-with-AI - App Review Analysis

## Project Overview
This is a part of the "Automating-Competitor-Tracking-with-AI" project where we aim to analyze app reviews to detect weak points in a competitor's application. This task uses Google Play Store reviews, performs sentiment analysis, and extracts common words from negative reviews to identify areas where the app could improve.

## Functionality
- **Fetch Reviews**: The script fetches the latest reviews of an app from the Google Play Store using the app's ID.
- **Sentiment Analysis**: Reviews are analyzed for sentiment (positive, neutral, or negative).
- **Weak Point Extraction**: The most common words in negative reviews are extracted to find potential weaknesses in the app.
- **Visualization**: A word cloud is generated to visually represent the most common weak points from the negative reviews.

## Prerequisites
Ensure the following libraries are installed:
- `requests`
- `beautifulsoup4`
- `textblob`
- `matplotlib`
- `wordcloud`

You can install these libraries using `pip`:

pip install requests beautifulsoup4 textblob matplotlib wordcloud
