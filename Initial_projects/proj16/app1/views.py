from django.shortcuts import render
from app1.forms import StudentForm
from django.http import HttpResponse

# Create your views here.

flag=True

def studview(request):
    global flag
    if flag:
       studform=StudentForm()
       flag=False
       return render(request,"student.html.",context={'stud':studform})
    else:
        flag=True
        studform=StudentForm(request.GET)
        if studform.is_valid():
            rollno=studform.cleaned_data['rollno']
            name=studform.cleaned_data['name']
            course=studform.cleaned_data['course']
            print(rollno,name,course)
        studform=StudentForm()    
        return render(request,"student.html",context={'stud':studform})
        
