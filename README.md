Competitor Intelligence System - AI and Automation Project

Project Overview

This project is a Competitor Intelligence System that automates the process of monitoring competitors’ activities by collecting and summarizing data from multiple sources, such as GitHub commits, job postings, app reviews, and pricing pages. The system uses AI synthesis for summarizing the collected data and displays the insights on a Notion dashboard for easy visualization.


Key Features

Data Collection: Collects data from multiple sources (GitHub, job postings, app reviews, pricing pages) and stores it in a Notion database.

AI Summarization: Uses AI to generate daily summaries from the collected data, making the insights easily digestible.

Notion Dashboard: Creates a visual dashboard in Notion to display key metrics and summarized insights.

Automation: Automates the entire workflow, from data collection to summarization and visualization, ensuring the system runs autonomously.

Technologies Used

Notion API: For fetching and updating data in the Notion database.

Hugging Face’s BART (or similar models): For AI-based text summarization.

Python: For automation, API interaction, and processing.

n8n (optional): For workflow automation.

Project Setup

Step 1: Install Dependencies
To get started, make sure you have Python installed, and then install the necessary libraries:

pip install requests notion-client transformers

Step 2: Notion API Setup
1.Go to the Notion Developers page.
2.Create a new integration and get your API key.
3.Share your database with the integration to grant it access.
4.Set the database ID in the environment variables or the script.

Step 3: Fetch Data from Notion

The project uses Notion API to fetch data. The following script retrieves the necessary data from your Notion database:

import requests
import json

NOTION_API_KEY = 'your_notion_api_key'
DATABASE_ID = 'your_notion_database_id'

def fetch_notion_data():
    headers = {
        'Authorization': f'Bearer {NOTION_API_KEY}',
        'Content-Type': 'application/json',
        'Notion-Version': '2021-05-13',
    }
    url = f'https://api.notion.com/v1/databases/{DATABASE_ID}/query'
    response = requests.post(url, headers=headers)
    data = response.json()

    # Process the data and extract relevant content
    return data

Step 4: AI Synthesis for Summarization

AI is used to generate daily summaries from the fetched data. This is achieved using the BART model from Hugging Face. The following function performs text summarization:

from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_data(text):
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']


The summarization process is triggered after fetching the data from Notion. It condenses large datasets into concise insights, which are then pushed back to Notion for visualization.

Step 5: Updating Data Back to Notion
Once the data is summarized, the results are updated in the Notion dashboard. This is done through the Notion API:

def update_notion_summary(summary_text):
    headers = {
        'Authorization': f'Bearer {NOTION_API_KEY}',
        'Content-Type': 'application/json',
        'Notion-Version': '2021-05-13',
    }
    url = f'https://api.notion.com/v1/pages'
    data = {
        "parent": { "database_id": DATABASE_ID },
        "properties": {
            "Summary": {
                "rich_text": [
                    {
                        "text": {
                            "content": summary_text
                        }
                    }
                ]
            }
        }
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()


Step 6: Creating a Notion Dashboard

The dashboard is designed to visually display key metrics and summarized data. Views are created in the Notion database to show different types of data:

GitHub Commits: Displays development speed insights.
Job Postings: Tracks strategy shifts based on hiring trends.
App Reviews: Shows weak points or areas of improvement in the competitor’s product.
Pricing Page Analysis: Tracks pricing changes for competitive positioning.

The following steps help you create the dashboard:

Create Different Views: Use Table or Timeline views to organize the data.
Use Roll-up Properties: To aggregate key metrics (e.g., average time between commits, total job postings).
Add Charts (Optional): For visual representation, you can integrate third-party tools like Google Sheets or Datawrapper for advanced charting.

Step 7: Automating the System
Automation can be achieved using n8n or other workflow automation tools to ensure the system runs without manual intervention. Tasks like:

Fetching data daily
Summarizing and updating the data

Managing API calls and responses

Step 8: Proof of API Usage
You can provide proof of using the Notion API by sharing screenshots of your Notion Developer API page. This ensures transparency and demonstrates that the system was built using Notion's official API.

Folder Structure

Here is the folder structure for your project:

competitor-intelligence-system/
├── README.md
├── notion_integration.py  # Notion API integration
├── ai_synthesis.py       # AI summarization script
├── dashboard_screenshot.png  # Screenshot of the Notion dashboard
└── requirements.txt      # Python dependencies


Screenshots

Notion Dashboard: A screenshot showing the Notion dashboard with different views and summarized data.
Notion Developer API Page: A screenshot proving that the Notion API was used for data fetching and updating.

Conclusion

This system automates the entire process of competitor tracking, from data collection and AI-based summarization to visualizing insights on a Notion dashboard. The entire workflow is automated and can run on autopilot, saving you time and effort compared to traditional methods.