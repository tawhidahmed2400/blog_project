from blog.models import contact
from django.shortcuts import render, HttpResponse
from datetime import datetime


def home(request):
    context = {
        "variable":"tawhid"
    }
    return render(request, 'temp.html', context)

def details(request):
    return render(request, 'details.html')
    #return HttpResponse("THIS IS DETAILS PAGE")

def profile(request):
    return render(request, 'profile.html' )
    

def register(request):
    return render(request, 'register.html')
    
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact_obj = contact( name=name, email=email, desc=desc, date=datetime.today())
        contact_obj.save()

    
    return render(request, 'contact.html')