from django.shortcuts import render
from app1.forms import StudentForm

# Create your views here.
def studview(request):
    studform=StudentForm()
    return render(request,"student.html.",context={'stud':studform})
