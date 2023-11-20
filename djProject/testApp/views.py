from django.shortcuts import render
from testApp.models import *

# Create your views here.
def home(request):
    return render(request,'testApp/home.html')

def hydjobs1(request):
    jobs_list=hydjobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'testApp/hydjobs.html',context=my_dict)

def bangalorejobs1(request):
    return render(request,'testApp/bangalorejobs.html')

def chennaijobs1(request):
    return render(request,'testApp/chennaijobs.html')

def punejobs1(request):
    return render(request,'testApp/punejobs.html')