from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def indexview(request):
    msg="<html><body bgcolor=cyan><h1>Index page</h1></body></html>"
    out=HttpResponse(msg)
    return out


def products(request):
    msg="<html><body bgcolor=yellow><h1>Products page</h1></body></html>"
    out=HttpResponse(msg)
    return out

