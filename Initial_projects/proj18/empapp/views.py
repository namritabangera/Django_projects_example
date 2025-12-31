from django.shortcuts import render,redirect
from empapp.models import EmpModel
from empapp.forms import Empform

# Create your views here.
def addemp(request):
    if request.method=='POST':
        form=Empform(request.POST)
        if form.is_valid():
            form.save()
            
            res=redirect('listemp')
            return res
    else:
        form=Empform()
        res=render(request,"addemp.html",context={'form':form})
        return res

def viewemp(request):
    emp=EmpModel.objects.all()
    res=render(request,"listemp.html",context={'emp':emp})
    return res

def editview(request,empno):
    print(empno)
    emp=EmpModel.objects.get(empno= empno)
    if request.method=='POST':
        form=Empform(request.POST,instance=emp)
        form.save()
        res=redirect('listemp')
        return res
    else:
        form=Empform(instance=emp) 
        res=render(request,"editemp.html",context={'form':form})
        return res
    

def delview(request,empno):
    print(empno)
    eno=EmpModel.objects.get(empno=empno)
    if request.method=='POST':
       
       eno.delete()
       res=redirect('listemp')
       return res
    form=Empform(instance=eno)
    res=render(request,"del.html",context={'form':form})
    return res


