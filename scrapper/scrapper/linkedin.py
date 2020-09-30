#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

Linkedin_List=[]
def getLinkedinApplyLink(href):
    try:
        prev=href
        page = requests.get(href)
        soup=BeautifulSoup(page.content,'html.parser')
        apply_link2 = soup.find('div', class_='topcard__content-right')
        url_elem=apply_link2.find('a')
        href=url_elem.get('href')
        if (href =="https://www.linkedin.com/uas/request-password-reset?trk=public_jobs_save-job_forgot_password"):
            return prev
        return href
    except:
        return href
        

def getURL(location,job_title):
    URL=''
    job_title=job_title.split()
    location=location.split(',')
    if len(job_title)==2 and len(location)==3:
        URL=URL+'https://in.linkedin.com/jobs/search?keywords='+job_title[0]+'%20'+job_title[1]+'&location='+location[0]+'%2C%20'+location[1]+'%2C%20'+location[2]+'&geoId=102510332&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0'
        return URL

    
def scrape(location,job_title):
    URL=getURL(location,job_title)
   
    page = requests.get(URL)
    print(page.status_code)
    soup=BeautifulSoup(page.content,'html.parser')
    
    results=soup.find(class_='jobs-search__results-list')
   
    job_elems = results.find_all('li', class_='result-card')
  
    for job_elem in job_elems:
      
        title_elem = job_elem.find('h3', class_='result-card__title')
        company_elem = job_elem.find('h4', class_='result-card__subtitle')
        location_elem = job_elem.find('span', class_='job-result-card__location')
        date = job_elem.find('time',class_='job-result-card__listdate')
        url_elem=job_elem.find('a')
        if date ==None:
            date = job_elem.find('time',class_='job-result-card__listdate--new')
        href=url_elem.get('href')
        link=getLinkedinApplyLink(href)
        
        Job_Dict={
        "title":title_elem.text.strip(),
        "company":company_elem.text.strip(),
        "location":location_elem.text.strip(),
        "apply_link":link,
        "date":date.text.strip()
        }
        Linkedin_List.append(Job_Dict)





