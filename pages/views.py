from django.shortcuts import render
from django.http import HttpResponse
from .models import Login
from .forms import LoginFrom
# Create your views here.

def index(request):
    #return HttpResponse("<h1>Welcome in our session</h1>")
    return render(request,"pages/index.html",{"age":99})


def about(request):
    lst=[3,4,5,7,8,9]
    dc={"name":"mosab","age":33,"lst":lst,"mark":55}
    return render(request,"pages/about.html",dc)

def addForm(request):
    if request.method=="POST":
        un=request.POST.get("un")
        pw=request.POST.get("pw")
        #register
        #login=Login(username=un,password=pw)
        #login.save()
        return render(request,"pages/success.html",
                      {"username":un,"password":pw})
    else:
        return render(request,"pages/form.html")
def lform(request):
    if request.method=="POST":
        un=request.POST.get("un")
        pw=request.POST.get("pw")
        #class Form 
        #login=Login(request.POST)
        #login.save()
        #register
        #login=Login(username=un,password=pw)
        #login.save()
        return render(request,"pages/success.html",
                      {"username":un,"password":pw})
    else:
        return render(request,"pages/Loginform.html",{"lf":LoginFrom})