# job-aggregator
It is a containerized web applicaton which scraps data from job portals and make available them at a single place.This application consist of two containers:

1. scrapper
2. web

## scrapper 
It provides a Rest API to get job data in json format.It is build in flask and saves data in sqlite database.Rest API is live at http://13.232.241.179/job_title/location
