import requests
from datetime import datetime, timedelta

# Replace with your token
TOKEN = "your personal access token here"

# Competitor's GitHub repository (update with the correct repo)
REPO = 'your repository name' # use your repo name

# GitHub API URL for repository commits
url = f'https://api.github.com/repos/{REPO}/commits'
headers = {'Authorization': f'token {TOKEN}'}

# Send a GET request to the API to fetch the last 100 commits
params = {'per_page': 100}  # You can change this to fetch more or fewer commits if needed
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    commits = response.json()
    print(f"Recent Commits for {REPO}:")
    
    # Initialize variables to calculate time differences
    time_differences = []
    commit_dates = []

    # Loop through commits to calculate time differences
    for i in range(1, len(commits)):
        latest_commit_date = commits[i-1]['commit']['author']['date']
        second_commit_date = commits[i]['commit']['author']['date']
        
        latest_commit_datetime = datetime.strptime(latest_commit_date, '%Y-%m-%dT%H:%M:%SZ')
        second_commit_datetime = datetime.strptime(second_commit_date, '%Y-%m-%dT%H:%M:%SZ')
        
        # Calculate time difference
        time_diff = latest_commit_datetime - second_commit_datetime
        time_differences.append(time_diff)
        
        # Store the date of the commits for later analysis
        commit_dates.append(latest_commit_datetime)

    # Calculate average time between commits
    if time_differences:
        avg_time_diff = sum(time_differences, timedelta()) / len(time_differences)
        print(f"\nAverage time between commits: {avg_time_diff}")

    # Calculate commits per week
    if commit_dates:
        start_date = commit_dates[-1]  # Earliest commit date
        end_date = commit_dates[0]     # Latest commit date
        total_weeks = (end_date - start_date).days // 7
        
        commits_per_week = len(commit_dates) / total_weeks if total_weeks > 0 else len(commit_dates)
        print(f"\nCommits per week: {commits_per_week:.2f} commits/week")

    # Print a few time differences to get an idea of commit frequency
    print("\nTime differences between consecutive commits:")
    for i, time_diff in enumerate(time_differences[:10]):  # Show first 10 time differences
        print(f"Commit {i+1} to Commit {i+2}: {time_diff}")

else:
    print(f"Error: Unable to fetch commits. Status Code: {response.status_code}")
