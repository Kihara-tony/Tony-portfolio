from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact,Projects
# Create your views here.


# Home/Index View
def index(request):
        return render(request, 'home.html')

def projects(request):
    projects = Projects.objects.all()
    return render(request,'projects.html',{'projects':projects})

def aboutme(request):
    return render(request,'aboutme.html')

def contact(request):
    return render(request,'contact.html')

