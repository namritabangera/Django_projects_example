from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
class TestView(View):
    def get(self,request):
        res=HttpResponse("Get Request")
        return res
    def post(self,request):
        res=HttpResponse("Post Request") 
        return res
    # def put(self,request):
    #     res=HttpResponse("Put Request")
    #     return res
    # def delete(self,request):
    #     res=HttpResponse("delete Request")
    #     return res
def display_temp(request):
        res=render(request,"test_temp.html",context={})
        return res
    
    
