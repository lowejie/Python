from bs4 import BeautifulSoup
import requests
import time

unfamiliar_skills = []
ask_unfamiliar = True
while ask_unfamiliar:
    print("Put some skills that you are not familiar with. Type 'no' to stop.")
    unfamiliar_skill = input('>')
    if unfamiliar_skill == "no":
        ask_unfamiliar = False
        print(f"Filtering out {unfamiliar_skills}")
    else:
        unfamiliar_skills.append(unfamiliar_skill)

def find_job():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()
            skills_raw = job.find('div', class_='more-skills-sections').text
            skills = ','.join(line.strip() for line in skills_raw.splitlines() if line.strip())
            skills_list = skills.split(',')
            more_info = job.header.h2.a['href']
            if not (set(unfamiliar_skills) & set(skills_list)):
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f"Company Name: {company_name} \n")
                    f.write(f"Required Skills: {skills} \n")
                    f.write(f"More Info: {more_info}")
                print(f'File saved: {index}')


if __name__ == '__main__':
    while True:
        find_job()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)