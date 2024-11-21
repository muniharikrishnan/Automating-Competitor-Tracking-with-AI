AI Synthesis for Daily Summaries

Overview

This project utilizes AI models for generating daily summaries from various datasets like GitHub commits, job postings, app reviews, and pricing page analysis. The AI synthesizes the extracted data into meaningful insights, which are then stored in Notion or another dashboard for visualization.

Purpose

The main objective of this script is to automate the summarization of large datasets. By leveraging AI, this process can turn raw data into concise, actionable summaries, helping to track competitors and monitor key metrics effectively.

Features

Fetches data from a Notion database or other data sources.

Splits large datasets into smaller chunks to comply with AI model token limits.

Uses a Hugging Face model (e.g., BART) or OpenAI GPT for summarization.

Sends the generated summary back to Notion or stores it for easy access.

Requirements

Python 3.x

transformers (Hugging Face library)

notion-client or Notion API to interact with your database

A Hugging Face account (for accessing the BART model)

OpenAI API key (if using GPT models)

Setup
1. Install Dependencies

Install the required Python libraries using pip:

pip install transformers notion-client openai

2. Notion API Setup

Obtain an integration token from Notion’s developers portal.
Share your Notion database with the integration.
Set up the Notion API client by creating a .env file with your Notion API token.

Example .env file:

NOTION_TOKEN=your_notion_integration_token

3. AI Model Setup

You can use either Hugging Face's BART model or OpenAI’s GPT-3/4 for summarization. Make sure to set up your Hugging Face API key or OpenAI key.

4. Environment Variables

Set the following variables in your .env file:

OPENAI_API_KEY=your_openai_api_key

5. Running the Script

To run the AI synthesis and summarization script, use the following command:

python ai_synthesis_summary.py

Script Breakdown

ai_synthesis_summary.py
T
his script performs the following:

Fetch Data: Extracts data from your Notion database (GitHub commits, job postings, reviews, etc.).

Pre-process Data: Handles large datasets by splitting them into smaller chunks.

Summarization: Sends the data to an AI model for summarization. You can choose between Hugging Face's BART or OpenAI GPT models.

Store Results: The generated summary is pushed back to Notion or saved to a file for easy review.

Example: Using Hugging Face's BART Model

from transformers import pipeline
import requests

# Fetch data from Notion (replace this with actual data extraction logic)
data = fetch_notion_data()

# Summarize data using BART
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
summary = summarizer(data)

# Send summarized content back to Notion
send_summary_to_notion(summary)

Example: Using OpenAI GPT-3/4 Mode

import openai

openai.api_key = "your-openai-api-key"

def summarize_with_gpt3(text):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=text,
      max_tokens=150
    )
    return response.choices[0].text.strip()


Error Handling

If the AI model returns an error due to large text, the script will automatically split the content into smaller chunks and reattempt summarization.

If the API request to Notion fails, the script will log the error and retry.


Output

Daily Summary: After successful execution, the script will generate a daily summary of your data and save it in Notion.

Example Output in Notion

Your Notion page will have a daily summary in a dedicated page or database, helping you keep track of key insights such as:

GitHub commit frequency
Job postings trends
Customer sentiment from reviews
Price changes from competitors

Example of a Notion Summary Output:

Date	Summary

2024-11-21	

The GitHub repository showed a steady increase in commits, with an average of 10 commits per week. Job postings indicate a shift towards hiring for AI-related roles. Recent app reviews highlighted performance issues in the latest release.
License

This project is open-source and available under the MIT License.

Contributing

Feel free to fork this project, raise issues, or submit pull requests for improvements.


