#!/usr/bin/env python
from scrapper import linkedin
from scrapper import monster
from scrapper import indeed
import server
import fields
import time

#scrapping data for given job boards and other intenet sites
while(True):
    def main():
        for location in fields.locations:
            for job_title in fields.job_titles:

                linkedin.scrape(location,job_title)
                monster.scrape(location,job_title)
                indeed.scrape(location,job_title)
                server.saveData()
                
    main()
    time.sleep(200000)
