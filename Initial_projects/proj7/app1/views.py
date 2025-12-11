from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display(request,name,age):
    msg=f'<h1>Name:{name} and Age:{age}</h1>'
    out=HttpResponse(msg)
    return out

