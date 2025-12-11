from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    msg="<html><body bgcolor=green><h1>Welcome to App2 Homepage</h1></body></html>"
    out=HttpResponse(msg)
    return out

def products(request):
    msg="<html><body bgcolor=blue><h1>Welcome to Apps Product page</h1></body></html>"
    out=HttpResponse(msg)
    return out

