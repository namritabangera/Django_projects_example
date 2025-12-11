from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view1(request):
    msg="<h2>Welcome to test Django page</h2>"
    out=HttpResponse(msg)
    return out
