from django.shortcuts import render

# Create your views here.
def index(request):
    resp=render(request,"index.html")
    return resp

def about(request):
    resp=render(request,"about.html")
    return resp

def contact(request):
    resp=render(request,"contacts.html")
    return resp

def course(request):
    resp=render(request,"course.html")
    return resp