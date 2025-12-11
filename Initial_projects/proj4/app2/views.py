from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view1(request):
    msg="<h1>View 1 of Application2</h1>"
    out=HttpResponse(msg)
    return out

def view2(request):
    msg="<h1>View 2 of Application2</h1>"
    out=HttpResponse(msg)
    return out