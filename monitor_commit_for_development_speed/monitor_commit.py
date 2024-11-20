import requests
from datetime import datetime, timedelta

# Function to fetch commits from GitHub
def get_github_commits(repo, token):
    url = f'https://api.github.com/repos/{repo}/commits'
    headers = {'Authorization': f'token {token}'}
    params = {'per_page': 100}  # You can change this to fetch more or fewer commits if needed
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching commits. Status Code: {response.status_code}")

# Function to calculate time differences between commits
def calculate_commit_frequencies(commits):
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
    
    return time_differences, commit_dates

# Function to calculate average time between commits
def calculate_avg_commit_time(time_differences):
    if time_differences:
        avg_time_diff = sum(time_differences, timedelta()) / len(time_differences)
        return avg_time_diff
    return None

# Function to calculate commits per week
def calculate_commits_per_week(commit_dates):
    if commit_dates:
        start_date = commit_dates[-1]  # Earliest commit date
        end_date = commit_dates[0]     # Latest commit date
        total_weeks = (end_date - start_date).days // 7
        
        return len(commit_dates) / total_weeks if total_weeks > 0 else len(commit_dates)
    return 0

# Main function to combine all logic
def monitor_commits(repo, token):
    commits = get_github_commits(repo, token)
    
    time_differences, commit_dates = calculate_commit_frequencies(commits)
    avg_time_diff = calculate_avg_commit_time(time_differences)
    commits_per_week = calculate_commits_per_week(commit_dates)
    
    return {
        "avg_time_diff": avg_time_diff,
        "commits_per_week": commits_per_week,
        "time_differences": time_differences[:10]  # Show first 10 time differences
    }
