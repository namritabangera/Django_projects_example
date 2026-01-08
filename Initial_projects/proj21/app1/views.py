from django.shortcuts import render

from app1.forms import Empform
from django.views import View
# Create your views here.
class EmpRegview(View):
    def get(self,request):
        form=Empform()
        res=render(request,"emp_reg.html",context={'form':form})
        return res
    
    def post(self,request):
        form=Empform(request.POST)
        if form.is_valid():
            form.save()
            form=Empform()
            res=render(request,"emp_reg.html",context={'form':form,'msg':'Emp added'})   
            return res    
        else:
           
            res=render(request,"emp_reg.html",context={'form':'form'})   
            return res

    