#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

def getLinkedinLink(href):

    try:

        page = requests.get(href)
        soup=BeautifulSoup(page.content,'html.parser')
        apply_link2 = soup.find('div', class_='topcard__content-right')
        url_elem=apply_link2.find('a')
        href=url_elem.get('href')
        return href
    except:
        return href
    
def linkedin():
    URL="https://in.linkedin.com/jobs/search?keywords=software%2Bdeveloper&location=Bengaluru%2C%2BKarnataka%2C%2BIndia&geoId=105307040&trk=public_jobs_jobs-search-bar_search-submit&currentJobId=2167051749&position=2&pageNum=0"
    page = requests.get(URL)
    print(page.status_code)
    soup=BeautifulSoup(page.content,'html.parser')
    
    results=soup.find(class_='jobs-search__results-list')
   
    job_elems = results.find_all('li', class_='result-card')
    count=0
    for job_elem in job_elems:
        count+=1
        title_elem = job_elem.find('h3', class_='result-card__title')
        
        company_elem = job_elem.find('h4', class_='result-card__subtitle')
        location_elem = job_elem.find('span', class_='job-result-card__location')
        date = job_elem.find('time',class_='job-result-card__listdate')
        url_elem=job_elem.find('a')
        if date ==None:
            date = job_elem.find('time',class_='job-result-card__listdate--new')
       
        
        href=url_elem.get('href')
        link=getLinkedinLink(href)
        print(title_elem.text.strip())
        print(company_elem.text.strip())
        print(location_elem.text.strip())
        print(link)
        print(date.text.strip())
        print(count)
        print("              ")





linkedin()