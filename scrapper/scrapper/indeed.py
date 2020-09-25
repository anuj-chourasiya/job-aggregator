#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup


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
    

def indeed():
    URL="https://www.indeed.co.in/jobs?q=software+developer&l=Bengaluru%2C+Karnataka"
    page = requests.get(URL)
    soup=BeautifulSoup(page.content,'html.parser')
    
    results=soup.find(id='resultsCol')
    
    job_elems = results.find_all('div', class_='jobsearch-SerpJobCard')
    for job_elem in job_elems:
        url_elem = job_elem.find('a', class_='jobtitle')
        title_elem = job_elem.find('a', class_='jobtitle')
        company_elem = job_elem.find('span', class_='company')
        location_elem = job_elem.find('span', class_='location accessible-contrast-color-location')
        date = job_elem.find('span', class_='date')
        href = url_elem.get('href')
        href="https://www.indeed.com"+href
        link=getIndeedApplyLink(href)
        if href is None:
	        continue
        print(title_elem.text.strip())
        print(company_elem.text.strip())
        print(location_elem.text.strip())
        print(link)
        print(date.text.strip())
        print("              ")
indeed()






