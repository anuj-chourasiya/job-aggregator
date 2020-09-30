#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

Indeed_List=[]
def getIndeedApplyLink(href):
    page = requests.get(href)
    soup=BeautifulSoup(page.content,'html.parser')
    try:
        apply_link1 = soup.find('div', id='applyButtonLinkContainer')
        apply_link2 = apply_link1.find('div', class_='icl-u-lg-hide')
        url_elem=apply_link2.find('a')
        href=url_elem.get('href')
        return href
    except:
        return href


def getURL(location,job_title):
    URL=''
    job_title=job_title.split()
    location=location.split(',')
    
    if len(job_title)==2 and len(location)>=2:
        URL=URL+'https://www.indeed.co.in/jobs?q='+job_title[0]+'+'+job_title[1]+'&l='+location[0]+'%2C+'+location[1]+''
        return URL


def scrape(location,job_title):
    URL=getURL(location,job_title)
    page = requests.get(URL)
    soup=BeautifulSoup(page.content,'html.parser')
    results=soup.find(id='resultsCol')
    job_elems = results.find_all('div', class_='jobsearch-SerpJobCard')
    
    for job_elem in job_elems:
        url_elem = job_elem.find('a', class_='jobtitle')
        title_elem = job_elem.find('a', class_='jobtitle')
        company_elem = job_elem.find('span', class_='company')
        date = job_elem.find('span', class_='date')
        href = url_elem.get('href')
        href="https://www.indeed.com"+href
        link=getIndeedApplyLink(href)
        if href is None:
	        continue
        
        Job_Dict={
        "title":title_elem.text.strip(),
        "company":company_elem.text.strip(),
        "location":location,
        "apply_link":link,
        "date":date.text.strip()
        }
        Indeed_List.append(Job_Dict)






