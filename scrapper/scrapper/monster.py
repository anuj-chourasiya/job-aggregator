#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

Monster_List=[]
'''def getMonsterApplyLink(href):


    page = requests.get(href)
    soup=BeautifulSoup(page.content,'html.parser')

    apply_link1 = soup.find('div', id='applyButtonLinkContainer')
    apply_link2 = apply_link1.find('div', class_='icl-u-lg-hide')

    url_elem=apply_link2.find('a')
    href=url_elem.get('href')

    return href
	'''

def getURL(location,job_title):
    URL=''
    job_title=job_title.split()  #spliiting job title based on space
    location=location.split(',') #splitting location based on commas
    
    if len(job_title)==2 and len(location)==3:
        URL=URL+"https://www.monster.com/jobs/search/?q="+job_title[0]+"-"+job_title[1]+"&where="+location[0]+"-"+location[1]+"-"+location[2]+""
        return URL


def scrape(location,job_title):
    URL=getURL(location,job_title)
    page = requests.get(URL)
    soup=BeautifulSoup(page.content,'html.parser')
    results=soup.find(id='ResultsContainer')
    job_elems = results.find_all('section', class_='card-content')

    for job_elem in job_elems:
        title_elem = job_elem.find('h2', class_='title')
        company_elem = job_elem.find('div', class_='company')
        location_elem = job_elem.find('div', class_='location')
        url_elem=job_elem.find('a')
        if None in (title_elem, company_elem, location_elem):
            continue
        href=url_elem.get('href')
        #link =getMonsterApplyLink(href)
        if href is None:
            continue
    
        Job_Dict={
        "title":title_elem.text.strip(),
        "company":company_elem.text.strip(),
        "location":location_elem.text.strip(),
        "apply_link":href,
        "source":"monster"
        }
        Monster_List.append(Job_Dict)

