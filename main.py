import time
import requests
from bs4 import BeautifulSoup

def find_jobs():
    # Get the html page
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?'
                             'searchType=personalizedSearch&from=submit&txtKeywords'
                             '=Java+%2C+Python&txtLocation=us&cboWorkExp1=0').text
    soup = BeautifulSoup(html_text, 'lxml')

    # Look for the desired criteria
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text

        if 'few' in published_date or 'today' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']

            with open(f'posts/{index}.txt', 'w') as f:
                f.write(f"Company Name: {company_name.strip()} \n")
                f.write(f"Required Skills: {skills.strip()} \n")
                f.write(f"More Info: {more_info.strip()} \n")
            print(f"File Saved: {index}")


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes....")
        time.sleep(time_wait * 60)
