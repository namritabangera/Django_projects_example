from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcomeview(request):
    msg="<h2>Welcome to Django</h2>"
    out=HttpResponse(msg)
    return out

def depositview(request):
    msg="<h2>Deposit View</h2>"
    out=HttpResponse(msg)
    return out

def withdrawview(request):
    msg="<h2>Withdraw View</h2>"
    out=HttpResponse(msg)
    return out
