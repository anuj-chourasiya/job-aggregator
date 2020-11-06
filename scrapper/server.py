#!/usr/bin/env python
from flask import Flask, request, jsonify
import flask_whooshalchemy as wa
from scrapper import monster
from scrapper import linkedin
from scrapper import indeed
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import exc
import os
import utils

#getting logger object
logger=utils.getParameters("scrapper.log")

#Init app
app= Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#Database
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =True
app.config['WHOOSH_BASE']='whoosh'

#Init db
db = SQLAlchemy(app)
#Init ma
ma=Marshmallow(app)


#class JobInfo
class JobInfo(db.Model):
    __searchable__ = ['Job_Title', 'Location']
    #id=db.Column(db.Integer,primary_key=True,nullable=False)
    Job_Title=db.Column(db.String(100),primary_key=True)
    Company_Name=db.Column(db.String(100),primary_key=True)
    Location=db.Column(db.String(100),primary_key=True)
    Apply_Link=db.Column(db.String(100),primary_key=True)
    Source=db.Column(db.String(100))
    Date=db.Column(db.String)

    def __init__(self,Job_Title,Company_Name,Location,Apply_Link,Source,Date):
        self.Job_Title=Job_Title
        self.Company_Name=Company_Name
        self.Location=Location
        self.Apply_Link=Apply_Link
        self.Source=Source
        self.Date=Date

wa.whoosh_index(app,JobInfo)

#JobInfo Schema
class JobInfoSchema(ma.Schema):
    class Meta:
        fields= ('Job_Title','Company_Name','Location','Apply_Link','Source','Date')

#Init Schema
job_info_schema=JobInfoSchema()
job_infos_schema=JobInfoSchema(many=True)

def saveData(all_data):
    
    logger.info("---------------------- {}".format(len(all_data)))

    for data in range(len(all_data)):
        
        try:
            new_jobInfo = JobInfo(all_data[data]['title'],all_data[data]['company'],all_data[data]['location'],all_data[data]['apply_link'],all_data[data]['source'],all_data[data]['date'])
            db.session.add(new_jobInfo)
            db.session.commit()
            logger.info("clean data".format(all_data[data]['title'],all_data[data]['location'],all_data[data]['source']))
        
            print("====================")
        except exc.IntegrityError:
            logger.info("inside redundant data")
            db.session.rollback()
        except:
            logger.warning("inside flusherror")
            db.session.rollback()

    logger.info("one cycle ends")
    all_data=[]


@app.route('/<string:job_title>/<string:location>',methods=['GET'])
def retireve_jobinfo(job_title,location):
    print("inside fun")
    query_parameters = request.args
    list_json=[]
    json_data={}
    results = JobInfo.query.whoosh_search(''+str(job_title)+' '+str(location)+'').all()    
    for data in results:
        json_data={
            "title":data.Job_Title,
            "company":data.Company_Name,
            "location":data.Location,
            "apply_linkh":data.Apply_Link,
            "source":data.Source,
            "date":data.Date
        }
        list_json.append(json_data)

    return jsonify(list_json)



#Run server
if __name__=='__main__':
    app.run(debug=True,host= '0.0.0.0')
