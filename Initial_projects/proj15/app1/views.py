from django.shortcuts import render

# Create your views here.
def view1(request):
    return render(request,"child1.html",context={})

def view2(request):
    return render(request,"child2.html",context={})

def view3(request):
    return render(request,"child3.html",context={})
