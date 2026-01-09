from django.shortcuts import render
from app1.models import EmpModel
from app1.forms import Empform
from django.views.generic import ListView

# Create your views here.
class EmpListView(ListView):
    model=EmpModel
    template_name="emp_list.html"
    context_object_name="emp"

    
