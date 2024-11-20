import requests
import json
from datetime import datetime

# Import data-fetching functions from subtask files
from monitor_commit import monitor_commits  # Changed function name from get_github_data to monitor_commits
from job_postings import get_job_posting_data  # Function from job_postings.py
from app_reviews import analyze_review_and_sentinment  # Function from app_reviews.py
from scan_pricing_pages import track_pricing_changes  # Function from scan_pricing_pages.py

# Define your Notion API token and database ID
notion_token = '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'
database_id = '1444973094b380a88451ee5a71e7d340'

# GitHub Personal Access Token and Repository Name (to be passed for monitoring commits)
github_token = 'your_github_token'  # Replace with your GitHub personal access token
github_repo = 'your_github_repo_name'  # Replace with the GitHub repository name (e.g., 'user/repo')

# Define the Notion API URL
url = 'https://api.notion.com/v1/pages'

# Function to get current date in ISO format
def get_current_date():
    return datetime.utcnow().isoformat()

# Function to synthesize data into a daily brief
def synthesize_data(competitor_data, job_posting_data, review_sentiment, pricing_changes):
    # Example of synthesizing data into a summary
    brief = (
        f"Competitor Updates: {competitor_data.get('summary', 'No updates.')}\n"
        f"Job Postings Insights: {job_posting_data.get('summary', 'No updates.')}\n"
        f"App Review Sentiments: {review_sentiment.get('summary', 'No updates.')}\n"
        f"Pricing Changes: {pricing_changes.get('summary', 'No updates.')}\n"
    )
    return brief

# Fetch data from previous subtask functions
competitor_data = monitor_commits(github_repo, github_token)  # Fetch GitHub commit data using monitor_commits function
job_posting_data = get_job_posting_data()  # Get job posting data from job_postings.py
review_sentiment = analyze_reviews_and_sentiment() # Get review sentiment analysis from app_reviews.py

# For pricing changes, use the scan_pricing_pages.py function
previous_data = None  # This would typically be persisted in a database or file
pricing_info = fetch_pricing_changes()  # Fetch current pricing data
pricing_changes, updated_data = track_pricing_changes(pricing_info, previous_data)  # Track and identify pricing changes

# Generate a daily brief using synthesized data
daily_brief = synthesize_data(competitor_data, job_posting_data, review_sentiment, pricing_changes)

# Prepare the data in Notion's expected format
data = {
    "parent": {"database_id": database_id},
    "properties": {
        "Competitor Name": {
            "title": [
                {
                    "text": {
                        "content": competitor_data.get('competitor_name', 'N/A')
                    }
                }
            ]
        },
        "Product Name": {
            "rich_text": [
                {
                    "text": {
                        "content": pricing_changes.get('product_name', 'N/A')
                    }
                }
            ]
        },
        "Pricing": {
            "rich_text": [
                {
                    "text": {
                        "content": pricing_changes.get('pricing', 'N/A')
                    }
                }
            ]
        },
        "Sentiment": {
            "rich_text": [
                {
                    "text": {
                        "content": review_sentiment.get('sentiment', 'N/A')
                    }
                }
            ]
        },
        "Date": {
            "date": {
                "start": get_current_date()
            }
        },
        "Daily Brief": {
            "rich_text": [
                {
                    "text": {
                        "content": daily_brief
                    }
                }
            ]
        }
    }
}

# Define headers for Notion API request
headers = {
    'Authorization': f'Bearer {notion_token}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28',  # Ensure you use the latest version of the API
}

# Send the request to the Notion API to create a new page (row) in the database
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check the response status
if response.status_code == 200:
    print("Data successfully added to Notion database.")
else:
    print(f"Error: {response.status_code}, {response.text}")
