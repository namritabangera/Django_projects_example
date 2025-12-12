from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calc(request):
    num1=eval(request.GET.get("n1"))
    num2=eval(request.GET.get("n2"))
    cmd=request.GET.get("b1")
    match(cmd):
        case "Add":
            num3=num1+num2
        case "Sub":
            num3=num1-num2
        case "mul":
            num3=num1*num2

        case "div":
            num3=num1/num2            

    # output=f'Result of {num1} and {num2} is {num3}'        

    return render(request,"result.html",context={'num1':num1,'num2':num2,'num3':num3})
    # resp=HttpResponse(output)
    

def index(request):
    out=render(request,"calc.html")
    return out
