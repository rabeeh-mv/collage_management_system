from django.shortcuts import render
from .models import Notification ,Facultie

# Create your views here.

def index(request):
    return render(request,'index.html')

def knowUs(request):
    return render(request,'know-us.html')

def Features(request):
    fact_list={
        'Features':Facultie.objects.all()
    }
    return render(request,'Features.html',fact_list)

def Admission(request):
    return render(request,'Admission.html')

def Academics(request):
    return render(request,'Academics.html')

def Students_Corner(request):
    return render(request,'Students-Corner.html')

def Notifications(request):
    not_list={
        'notification':Notification.objects.all()
    }
    return render(request,'Notifications.html', not_list)

def Downloads(request):
    return render(request,'Downloads.html')

def Gallery(request):
    gallery={
        'not':Notification.objects.all(),
         'Features':Facultie.objects.all()
    }
    return render(request,'Gallery.html',gallery)

def videos(request):
    return render(request,'videos.html')