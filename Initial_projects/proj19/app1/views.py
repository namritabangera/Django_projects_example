from django.shortcuts import render
from app1.forms import EmailForm,CustomerForm
# Create your views here.
def emailview(request):
    if request.method=='POST':
       form=EmailForm(request.POST)
       if form.is_valid():
          res=render(request,"valid_temp.html",context={'msg':'input data is valid'})
          return res
       else:
          res=render(request,"email_temp.html",context={'form':form})
          return res
    form=EmailForm()   
    res=render(request,"email_temp.html",context={'form':form})
    return res

def custview(request):
   msg='yet to save'
   if request.method=='POST':
       form=CustomerForm(request.POST)
       if form.is_valid():
          form.save()
          print("Data saved to db")
          msg="Customer Data saved"
          form=CustomerForm()
          res=render(request,"cust_temp.html",context={'form':form,'msg':msg})
          return res
       else:
         msg='error' 
         print("error in saving form to db")
         res=render(request,"cust_temp.html",context={'form':form,'msg':msg})
         return res
   form=CustomerForm()    
   res=render(request,"cust_temp.html",context={'form':form,'msg':msg})
   return res
   


