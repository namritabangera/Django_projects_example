from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def add(request,n1,n2):
    n3=int(n1)+int(n2)
    msg=f'<h1>Sum of {n1} and {n2} is {n3}</h1>'
    out=HttpResponse(msg)
    return out

    