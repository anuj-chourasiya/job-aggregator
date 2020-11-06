#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import sys
sys.path.append("/root")
import utils


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
    
    if len(job_title)==2 and len(location)==3:
        URL=URL+'https://www.indeed.co.in/jobs?q='+job_title[0]+'+'+job_title[1]+'&l='+location[0]+'%2C+'+location[1]+''
        return URL
    if len(job_title)==2 and len(location)==4:
        URL=URL+'https://www.indeed.co.in/jobs?q='+job_title[0]+'+'+job_title[1]+'&l='+location[0]+'%2C+'+location[1]+'%2C+'+location[2]+'%2C+'+location[3]+''
        return URL

logger=utils.getParameters("scrapper.log")
#scrape function fill scrapped data in a list
def scrape(location,job_title):
    Indeed_List=[]

    #getting site specefic url
    URL=getURL(location,job_title)
    page = requests.get(URL)
    if page.status_code != 200:
        logger.warning("status code: {} for location: {} and job_title: {}".format(page.status_code,location,job_title))
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
        #getting apply link by scrapping again
        link=getIndeedApplyLink(href)
        if href is None:
	        continue
        
        #creating dictionary for job information 
        Job_Dict={
        "title":title_elem.text.strip(),
        "company":company_elem.text.strip(),
        "location":location,
        "apply_link":link,
        "source":"indeed",
        "date":date.text.strip()
        }
        Indeed_List.append(Job_Dict)
    return Indeed_List






