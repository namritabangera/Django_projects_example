from django.shortcuts import render
from empapp.models import EmpModel

# Create your views here.
def indexview(request):
    out=render(request,"index.html",context={})
    return out

def addview(request):
    msg=""
    out=render(request,"addemp.html",context={'msg':msg})
    return out

def updateview(request):

    out=render(request,"update.html",context={})
    return out

def delemp(request):
    out=render(request,"delete.html",context={})
    return out

def viewemp(request):
    q1=EmpModel.objects.all()
    out=render(request,"viewemp.html",context={'q1':q1})
    return out

def insertemp(request):
    msg=""
    empno=request.GET.get('empno')
    empname=request.GET.get('empname')
    empjob=request.GET.get('empjob')
    empsal=request.GET.get('empsal')
    EmpModel.objects.create(empno=empno,empname=empname,empjob=empjob,empsal=empsal)
    msg="Employee Added"
    out=render(request,"addemp.html",context={'msg':msg})
    return out

def updatempview(request):
    empno=request.GET.get('empno')
    empsal=request.GET.get('empsal')
    q1=EmpModel.objects.get(empno=empno)
    q1.empsal=empsal
    q1.save()
    msg="Employee details "+empno+" updated"
    out=render(request,"update.html",context={'msg':msg})
    return out

def deleterequest(request):
    empno=request.GET.get('empno')
    q=EmpModel.objects.get(empno=empno)
    q.delete()
    msg="Emp "+ empno+" deleted"
    out=render(request,"delete.html",context={'msg':msg})
    return out
