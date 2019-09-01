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

# def send_welcome_email(name,receiver):
#     # Creating message subject and sender
#     subject = 'Welcome to the MoringaTribune NewsLetter'
#     sender = 'james@moringaschool.com'
#     #passing in the context vairables
#     text_content = render_to_string('email/newsemail.txt',{"name": name})
#     html_content = render_to_string('email/newsemail.html',{"name": name})

#     msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
#     msg.attach_alternative(html_content,'text/html')
#     msg.send()