GitHub Repository Commit Analysis Tool
Overview
This Python script analyzes the commit history of a specified GitHub repository. By leveraging the GitHub API, it fetches recent commits and calculates metrics such as:

Average time between commits.
Commit frequency (commits per week).
Time differences between consecutive commits.
The script helps to understand the activity level and commit patterns of a repository, making it useful for project tracking or competitor analysis.

Features
Fetches up to 100 recent commits from a GitHub repository.
Calculates:
Average time interval between consecutive commits.
Commit frequency in terms of commits per week.
Displays the time differences for the first 10 consecutive commits.
Helps analyze repository activity trends.
Prerequisites
1. Python Dependencies:
Install required Python libraries using:
bash
Copy code
pip install requests
2. GitHub Personal Access Token:
Generate a token from GitHub Developer Settings with repo scope.
Replace your personal access token here in the script with your generated token.
3. Repository Name:
Replace your repository name with the full name of the repository (e.g., username/repository-name).
How to Use
Clone or Copy the Script:

Save the script in a .py file, for example: commit_analysis.py.
Run the Script:

Execute the script using:
bash
Copy code
python commit_analysis.py
View Results:

The script outputs:
Recent commits for the repository.
Average time between commits.
Commit frequency (commits per week).
Time differences between consecutive commits.
Sample Output
Here is an example of what the script outputs:

sql
Copy code
Recent Commits for username/repository-name:

Average time between commits: 1 day, 5:32:00
Commits per week: 12.5 commits/week

Time differences between consecutive commits:
Commit 1 to Commit 2: 1 day, 3:45:00
Commit 2 to Commit 3: 0:45:00
...
Important Notes
API Rate Limits: The GitHub API has a rate limit of 5000 requests per hour when authenticated with a personal token. Ensure your usage stays within this limit.
Data Accuracy: The script assumes a continuous chronological order of commits in the repository.
License
This project is licensed under the MIT License. See the LICENSE file for details.