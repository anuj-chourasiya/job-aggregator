#!/usr/bin/env python
import requests

from bs4 import BeautifulSoup

'''def getMonsterApplyLink(href):


    page = requests.get(href)
    soup=BeautifulSoup(page.content,'html.parser')

    apply_link1 = soup.find('div', id='applyButtonLinkContainer')
    apply_link2 = apply_link1.find('div', class_='icl-u-lg-hide')

    url_elem=apply_link2.find('a')
    href=url_elem.get('href')

    return href
	'''




def monster():
	URL="https://www.indeed.co.in/software-developer-jobs-in-Indore,-Madhya-Pradesh"
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
	print(title_elem.text.strip())
	print(company_elem.text.strip())
	print(location_elem.text.strip())
	print(href)

monster()