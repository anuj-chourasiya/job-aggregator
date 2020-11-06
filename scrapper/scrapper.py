#!/usr/bin/env python
from scrapper import linkedin
from scrapper import monster
from scrapper import indeed
import server
import fields
import time
import utils

logger=utils.getParameters("scrapper.log")
#scrapping data for given job boards and other intenet sites
while(True):
    def main():
        for location in fields.locations:
            for job_title in fields.job_titles:
                logger.info("calling scrape for location {} and job title {}".format(location,job_title))
                
                linked_data=linkedin.scrape(location,job_title)
                logger.info("linked in data: {}".format(linked_data))
                monster_data=monster.scrape(location,job_title)
                logger.info("monster data: {}".format(monster_data))
                indeed_data=indeed.scrape(location,job_title)
                logger.info("indeed data: {}".format(indeed_data))

                all_data=[]
                all_data.extend(linked_data)
                all_data.extend(monster_data)
                all_data.extend(indeed_data)

                server.saveData(all_data)
                
    main()
    time.sleep(21600)
