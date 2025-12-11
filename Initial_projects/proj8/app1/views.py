from django.shortcuts import render

# Create your views here.
def index(request):
    resp=render(request,"index.html",context={})
    return resp

