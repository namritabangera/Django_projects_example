from django.shortcuts import render

# Create your views here.
def view1(request):
    rollno=1
    sname="saisha"
    course="python"
    stud1={'rollno':rollno,'sname':sname,'course':course}
    out=render(request,"dtl1.html",context={'stud1':stud1})
    return out


def view2(request):
    a=100
    b=200
    out=render(request,"dtl2.html",context={'a':a,'b':b})
    return out

def view3(request):
    name="naresh"
    avg=90
    out=render(request,"dtl3.html",context={'name':name,'avg':avg    })
    return out

def view4(request):
    email=["nams@alfifavisa.com","rajeshbangera99@gmail.com","amrita2084@yahoo.com"]    
    out=render(request,"dtl4.html",context={'email':email})
    return out

def view5(request):
    marks={'suresh':[40,50,60],'naresh':[50,60,80],'rajesh':[60,70,45]}
    out=render(request,"dtl5.html",context={'marks':marks})
    return out

def view6(request):
    A=[10,20,30,40,50]
    B={'x':10,'y':20,'z':30}
    res = render(request,"dtl6.html",context={'A':A,'B':B})
    return res

