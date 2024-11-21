import requests
from transformers import pipeline
import textwrap

# Initialize the Hugging Face summarization pipeline (using BART model)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Notion API setup
NOTION_API_KEY = 'your_notion_integration_token'  # Replace with your Notion integration token
DATABASE_ID = 'your_notion_database_id'  # Replace with your database ID

# Headers for the Notion API
headers = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}

# Function to fetch data from Notion database
def fetch_data_from_notion():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    response = requests.post(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data['results']  # Returns list of database entries
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return []

# Function to extract content from fetched Notion data (adjusted for your schema)
def extract_content_from_notion_data(data):
    content = {
        "github_commits": [],
        "job_postings": [],
        "app_reviews": [],
        "pricing_info": []
    }

    for page in data:
        if 'properties' in page:
            # Extract GitHub commits
            if 'GitHub Commits' in page['properties']:
                github_commits = page['properties']['GitHub Commits']['rich_text']
                if github_commits:
                    content["github_commits"].append(github_commits[0]['text']['content'])
            
            # Extract Job postings
            if 'Job Postings' in page['properties']:
                job_postings = page['properties']['Job Postings']['rich_text']
                if job_postings:
                    content["job_postings"].append(job_postings[0]['text']['content'])
            
            # Extract App reviews
            if 'App Reviews' in page['properties']:
                app_reviews = page['properties']['App Reviews']['rich_text']
                if app_reviews:
                    content["app_reviews"].append(app_reviews[0]['text']['content'])
            
            # Extract Pricing information
            if 'Pricing Info' in page['properties']:
                pricing_info = page['properties']['Pricing Info']['rich_text']
                if pricing_info:
                    content["pricing_info"].append(pricing_info[0]['text']['content'])
    
    return content

# Function to combine all content into a single text for summarization
def combine_content_for_summarization(content):
    combined_text = ""
    combined_text += "GitHub Commits:\n" + "\n".join(content["github_commits"]) + "\n\n"
    combined_text += "Job Postings:\n" + "\n".join(content["job_postings"]) + "\n\n"
    combined_text += "App Reviews:\n" + "\n".join(content["app_reviews"]) + "\n\n"
    combined_text += "Pricing Info:\n" + "\n".join(content["pricing_info"]) + "\n\n"
    return combined_text

# Function to split text into smaller chunks (ensuring token limits are respected)
def split_text_into_chunks(text, max_chunk_size=1024):
    return textwrap.wrap(text, width=max_chunk_size, break_long_words=False)

# Function to summarize large data
def summarize_large_data(data, max_chunk_size=1024):
    # Split the data into smaller chunks if it's too large
    chunks = split_text_into_chunks(data, max_chunk_size)
    
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=150, min_length=50, do_sample=False)
        summaries.append(summary[0]['summary_text'])
    
    # Combine the summaries into one final summary
    final_summary = ' '.join(summaries)
    return final_summary

# Main Function to Fetch Data and Summarize it
def main():
    # Fetch data from Notion
    notion_data = fetch_data_from_notion()
    
    if notion_data:
        # Extract content from the Notion data based on your database schema
        extracted_content = extract_content_from_notion_data(notion_data)
        
        # Combine all content into one text
        combined_text = combine_content_for_summarization(extracted_content)
        
        # Summarize the large data
        summary = summarize_large_data(combined_text)
        
        print("Final Summary: ")
        print(summary)
    else:
        print("No data to summarize.")

if __name__ == "__main__":
    main()
