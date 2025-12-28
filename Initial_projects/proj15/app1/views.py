from django.shortcuts import render

# Create your views here.
def view1(request):
    return render(request,"child1.html",context={})

def view2(request):
    return render(request,"child2.html",context={})

def view3(request):
    return render(request,"child3.html",context={})

def home(request):
    return render(request,"home.html",context={})

def course(request):
    return render(request,"course.html",context={})

def contacts(request):
    return render(request,"contacts.html",context={})


def calc(request):
    return render(request,"calc.html")
