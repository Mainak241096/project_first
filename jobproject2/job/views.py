from django.shortcuts import render
from job.models import Development,Hacking,DebugTester
# Create your views here.
def index_view(request):
    return render(request,'jobapp/index.html')

def development_view(request):
    jobs_list = Development.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'jobapp/development.html',my_dict)

def debug_view(request):
    jobs_list = DebugTester.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'jobapp/debug.html',my_dict)

def hacking_view(request):
    jobs_list = Hacking.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'jobapp/hacking.html',my_dict)
