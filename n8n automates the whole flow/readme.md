# Daily Competitor Market Brief Automation (n8n)

## Overview
The **Daily Competitor Market Brief Automation** is an n8n workflow that automates the collection of competitor data and generates a daily brief summarizing key market intelligence. The automation collects information on competitor pricing, job postings, app review sentiment, and development speed. The resulting brief is sent via Slack or email, helping businesses stay updated with competitor movements.

## Features
- **Competitor Pricing Tracking**: Automatically scrapes competitor pricing pages for changes.
- **Job Posting Trends**: Scrapes job boards to analyze competitor hiring trends.
- **Sentiment Analysis**: Analyzes app reviews to identify competitor weaknesses.
- **Development Speed Monitoring**: Tracks competitor GitHub repositories for commit frequency.
- **Daily Brief Generation**: Synthesizes the data into a daily report and sends it via Slack or email.

## Use Cases
- **Market Intelligence**: Stay updated with competitor activities and market trends.
- **Strategic Decision Making**: Adjust pricing, hiring, and development strategies based on competitor insights.
- **Competitor Analysis**: Monitor competitor product pricing, sentiment, and development speed.

## Requirements
- n8n (installed locally or hosted)
- Google Sheets (for storing pricing data)
- GitHub API (for tracking commit frequency)
- Slack (for sending the daily brief)

## How to Use
1. **Clone or Download** the n8n workflow file.
2. **Set up** the necessary credentials and APIs (e.g., Google Sheets, GitHub, Slack).
3. **Import** the workflow into n8n.
4. **Configure** the nodes with appropriate values (URLs, API keys, etc.).
5. **Execute** the workflow to automate the collection and generation of the daily market brief.

## Script Breakdown
- **Competitor Pricing Tracking**: Scrapes competitor websites for pricing information.
- **Job Posting Tracking**: Scrapes job posting sites like LinkedIn or AngelList.
- **Sentiment Analysis**: Uses TextBlob to perform sentiment analysis on app reviews.
- **GitHub Commit Tracking**: Monitors GitHub commits to assess the development speed of competitors.
- **Report Generation**: The final output is a report sent via Slack, containing key insights from all sources.

## Customization
- **Adding New Competitors**: Extend the workflow by adding new HTTP Request nodes for additional competitors.
- **Visualization**: Customize the output format or add new visualization nodes (e.g., for charts).

## License
This project is licensed under the MIT License - see the LICENSE file for details.
