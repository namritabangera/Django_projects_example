from django.shortcuts import render
from app1.models import EmpModel
from app1.forms import Empform
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView,ListView
from django.urls import reverse_lazy,reverse
from django.http import Http404,HttpResponse
# Create your views here.
class EmpListView(ListView):
    model=EmpModel
    template_name="emp_list.html"
    context_object_name="emp"

class EmpCreateView(CreateView):
    model=EmpModel
    template_name='emp_create.html'
    success_url=reverse_lazy('listemp')
    form_class= Empform
    

class EmpUpdateView(UpdateView):
    model=EmpModel
    template_name='emp_update.html'
    success_url=reverse_lazy('listemp')
    form_class=Empform
   
    

class EmpDelView(DeleteView):
    model=EmpModel
    template_name='emp_del.html'
    success_url=reverse_lazy('listemp')
    context_object_name="emp"

class EmpDetails(DetailView):
    model=EmpModel
    template_name='emp_details.html'
    context_object_name="emp"
    

class EmpListView1(ListView):
    model=EmpModel
    template_name="emp_list.html"
    context_object_name="emp"
    def get_queryset(self):
        qs=self.model.objects.filter(job="hr")
        return qs
    

class EmpListView2(ListView):
    model=EmpModel
    template_name="emp_list.html"
    context_object_name="emp"
    def get_queryset(self):
        value=self.kwargs.get('job')
        print("Values=",value)
        qs=self.model.objects.filter(job=value)
        return qs

class EmpListView3(ListView):
    model=EmpModel
    template_name="emp_list.html"        
    context_object_name="emp"
    def get_queryset(self):
        job=self.request.GET.get('job')
        qs=self.model.objects.filter(job=job)
        return qs
    
def joblist(request):
        res=render(request,"empjob_temp.html",context={})
        return res

class EmpDetailsView1(DetailView):
    model=EmpModel
    template_name="emp_details.html" 
    context_object_name="emp"
    #calling the super class func get 
    def get(self,request,*vargs,**kwargs):
        try:
            res=super().get(request,vargs,kwargs)
            return res 
        except:
            return HttpResponse("InvalidEmployeeNo")
    #over riding the get_object method
    def get_object(self):
        eno=self.kwargs.get('pk')
        try:
            obj=self.model.objects.get(empno=eno)
            return obj
        except:
            raise Http404("Invalid Employee No")    
        