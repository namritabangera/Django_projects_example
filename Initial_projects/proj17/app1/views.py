from django.shortcuts import render
from app1.forms import RegisterForm
# Create your views here.
flag=True
def register_view(request):
    global flag
    if flag:
        form=RegisterForm()
        res=render(request,"register.html",context={'form':form})
        flag=False
        return res
    else:
        form=RegisterForm(request.GET)
        if form.is_valid():
            uname=form.cleaned_data['uname']
            print(f'{uname} regisration is complete')
        else:
            res=render(request,"register.html",context={'form':form})    
            return res
        form=RegisterForm()
        return render(request,"register.html",context={'form':form})
    

            