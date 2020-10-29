from django.shortcuts import render
from django.views import View
from django.core.paginator import  Paginator
import requests


class HomeView(View):

    template_name="home/main.html"
    def post(self,request,page=1):
        job_title=request.POST.get('job_title')
        print("job_title",job_title)
        location=request.POST.get('location')
        print("location",location)
        ctx={}
        if job_title and location:
            
            data= requests.get('http://13.235.49.91/'+job_title+'/'+location)
            print(data.status_code)
            data=data.json()
            print(data[0]['company'])
            paginator=Paginator(data,20)
            print(paginator.num_pages)
            #page=request.GET.get(page)
        
            data=paginator.get_page(page)
            print(data.number) 
            ctx['data']=data
            ctx["title"]=job_title
            ctx["location"]=location

        else:
            ctx["data"]=None
            ctx["title"]=job_title
            ctx["location"]=location
       
        

        return render(request,self.template_name,ctx)
        
    def get(self,request):
        job_title=request.GET.get('job_title')
        location=request.GET.get('location')
        page=request.GET.get('page')
        print("location",page)


        if job_title is not None:
            
            ctx={}
            data= requests.get('http://13.235.49.91/'+job_title+'/'+location)
            print(data.status_code)
            data=data.json()
            print(data[0]['company'])
            paginator=Paginator(data,20)
            print(paginator.num_pages)
            #page=request.GET.get(page)
            print("page",page)
            data=paginator.get_page(page)
            print(data.number)
            ctx['data']=data
            ctx["title"]=job_title
            ctx["location"]=location
            return render(request,self.template_name,ctx)

        print("inside else")

        return render(request,self.template_name)
