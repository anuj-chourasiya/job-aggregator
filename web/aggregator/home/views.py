from django.shortcuts import render
from django.views import View
import requests


class HomeView(View):
    template_name="home/main.html"
    def post(self,request):
        job_title=request.POST.get('job_title')
        print("job_title",job_title)
        location=request.POST.get('location')
        print("location",location)
        ctx={}
        if job_title and location:
            data= requests.get('http://13.232.241.179/'+job_title+'/'+location)
            print(data.status_code)
            ctx["data"]=data.json
            ctx["title"]=job_title
            ctx["location"]=location

        else:
            ctx["data"]=None
            ctx["title"]=job_title
            ctx["location"]=location

        return render(request,self.template_name,ctx)
    def get(self,request):
        return render(request,self.template_name)
