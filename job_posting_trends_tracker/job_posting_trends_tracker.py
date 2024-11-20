import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import matplotlib.pyplot as plt
import time

# --- LinkedIn Jobs API (using PhantomBuster) ---
# Note: LinkedIn Jobs API requires third-party service (e.g., PhantomBuster) as official API is limited.
def get_linkedin_jobs():
    print("Getting LinkedIn Jobs using PhantomBuster...")
    # Use PhantomBuster LinkedIn Job scraping or use LinkedIn API
    # For example, you would have your PhantomBuster setup here
    pass  # Placeholder for LinkedIn job scraping


# --- Indeed API ---
def get_indeed_jobs(api_key):
    print("Getting jobs from Indeed API...")
    url = f'https://api.indeed.com/ads/apisearch?publisher={api_key}&q=developer&l=san+francisco&format=json'
    response = requests.get(url)
    data = response.json()

    if 'results' in data:
        for job in data['results']:
            print(f"Job Title: {job['jobtitle']}, Location: {job['location']}")
    else:
        print("No jobs found on Indeed.")


# --- Glassdoor API ---
def get_glassdoor_jobs(api_key):
    print("Getting jobs from Glassdoor API...")
    url = f'https://api.glassdoor.com/api/api.htm?t.p={api_key}&t.k={api_key}&userip=0.0.0.0&useragent=Mozilla&action=employers&name=Google'
    response = requests.get(url)
    data = response.json()

    if 'response' in data:
        for job in data['response'].get('employers', []):
            print(f"Job Title: {job['name']}, Location: {job['location']}")
    else:
        print("No jobs found on Glassdoor.")


# --- ZipRecruiter API ---
def get_ziprecruiter_jobs(api_key):
    print("Getting jobs from ZipRecruiter API...")
    url = f'https://api.ziprecruiter.com/jobs/v1?api_key={api_key}&search=developer&location=san+francisco'
    response = requests.get(url)
    data = response.json()

    if 'jobs' in data:
        for job in data['jobs']:
            print(f"Job Title: {job['job_title']}, Company: {job['company_name']}, Location: {job['location']}")
    else:
        print("No jobs found on ZipRecruiter.")


# --- Web Scraping for Platforms without APIs ---
def scrape_angel_list():
    print("Scraping AngelList Jobs...")
    url = 'https://angel.co/jobs'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    job_titles = []
    job_listings = soup.find_all('li', class_='job_listings')
    for job in job_listings:
        job_title = job.find('h3').text.strip()
        job_titles.append(job_title)
        company = job.find('p', class_='startup').text.strip()
        print(f"Job Title: {job_title}, Company: {company}")

    return job_titles


def scrape_crunchboard():
    print("Scraping Crunchboard Jobs...")
    url = 'https://www.crunchbase.com/jobs'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    job_listings = soup.find_all('li', class_='job_list')
    for job in job_listings:
        job_title = job.find('h3').text.strip()
        company = job.find('a', class_='company').text.strip()
        print(f"Job Title: {job_title}, Company: {company}")


def scrape_stackoverflow_jobs():
    print("Scraping Stack Overflow Jobs...")
    url = 'https://stackoverflow.com/jobs'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    job_listings = soup.find_all('div', class_='listResults')
    for job in job_listings:
        job_title = job.find('a', class_='s-link').text.strip()
        company = job.find('div', class_='fc-black-500').text.strip()
        print(f"Job Title: {job_title}, Company: {company}")


def scrape_we_work_remotely():
    print("Scraping We Work Remotely Jobs...")
    url = 'https://weworkremotely.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    job_listings = soup.find_all('section', class_='jobs')
    for job in job_listings:
        job_title = job.find('h2').text.strip()
        company = job.find('h3').text.strip()
        print(f"Job Title: {job_title}, Company: {company}")


def scrape_remotive():
    print("Scraping Remotive Jobs...")
    url = 'https://remotive.io/remote-jobs'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    job_listings = soup.find_all('div', class_='job-listing')
    for job in job_listings:
        job_title = job.find('h3').text.strip()
        company = job.find('span', class_='company').text.strip()
        print(f"Job Title: {job_title}, Company: {company}")


def scrape_robert_half():
    print("Scraping Robert Half Jobs...")
    url = 'https://www.roberthalf.com/jobs'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    job_listings = soup.find_all('div', class_='job-card')
    for job in job_listings:
        job_title = job.find('h3').text.strip()
        company = job.find('div', class_='company').text.strip()
        print(f"Job Title: {job_title}, Company: {company}")


# --- Job Trends Tracking Function ---
def track_job_trends():
    job_trends = defaultdict(int)
    job_titles = scrape_angel_list()  # Scraping jobs from AngelList (you can add other platforms here)

    # Counting frequency of each job title
    for title in job_titles:
        job_trends[title] += 1

    return job_trends


# --- Plotting Job Posting Trends ---
def plot_job_trends(job_trends):
    # Plot the trends of job titles over time
    job_titles = list(job_trends.keys())
    job_counts = list(job_trends.values())

    plt.figure(figsize=(10, 6))
    plt.barh(job_titles, job_counts, color='skyblue')
    plt.xlabel('Number of Postings')
    plt.ylabel('Job Titles')
    plt.title('Job Posting Trends (AngelList)')
    plt.show()


# --- Main Function to Execute the Tracking ---
def main():
    # API keys for Indeed, Glassdoor, ZipRecruiter (replace with actual API keys)
    indeed_api_key = 'your_indeed_api_key'
    glassdoor_api_key = 'your_glassdoor_api_key'
    ziprecruiter_api_key = 'your_ziprecruiter_api_key'

    # Fetch job data from APIs (where available)
    get_indeed_jobs(indeed_api_key)
    get_glassdoor_jobs(glassdoor_api_key)
    get_ziprecruiter_jobs(ziprecruiter_api_key)

    # Scrape job data from websites without APIs
    scrape_angel_list()
    scrape_crunchboard()
    scrape_stackoverflow_jobs()
    scrape_we_work_remotely()
    scrape_remotive()
    scrape_robert_half()

    # Track and plot job trends
    print("Tracking Job Posting Trends...")
    job_trends = track_job_trends()
    plot_job_trends(job_trends)

    # Wait for a certain interval before tracking again (e.g., every 24 hours)
    time.sleep(86400)  # 24 hours


if __name__ == "__main__":
    main()
