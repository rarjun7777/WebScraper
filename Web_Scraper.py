#Importing the beautifulsoup and requests libraries 
#prettify , find_all and many more inbuilt functions can be used to extract the required data

import requests
from bs4 import BeautifulSoup
import time

print('Put some skill that you are not familiar with') 
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')


def find_jobs():

    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')    #finding the data using find_all function by specifying the tag and classname

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text    #span.text makes it print the text instead of semi structured data ( html tags )
        if 'few' in published_date:
            company_name = job.find(
                'h3', class_='joblist-comp-name').text.replace(' ', '')      #replace or strip is used to avoid whitespaces 
            skills = job.find(
                'span', class_='srp-skills').text.replace(' ', '')           
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'Profs/{index}.txt', 'w') as f:
                    f.write(f"Company Name : {company_name.strip()}\n")
                    f.write(f"Required Skills: {skills.strip()}\n")
                    f.write(f'More Info: {more_info}\n')

                    print(f'File saved: {index}')

                    
 #An if condition used to halt the programm for a while and continues its programm after the mentioned time 

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes.... ')
        time.sleep(time_wait * 60)