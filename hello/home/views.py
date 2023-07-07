from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    # we are using this to pass variable value but usually we don't use this varibale passing like this
    # we usually use to pass the database data in this context.
    context = {
        'variable1': "Raj is great",
        "variable2": "Abhishek is great"
    }
    return render(request, 'index.html', context)
    # return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is services page")

def contact(request):
    # to post the method to database
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        # import Contact from models and sending above parameter to those method to perform data saving to database
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        # method to save form
        contact.save()
        # to flash messages once data got delivered. To make user informed that data has been sent to database
        # where this is the alert method to display message. but for this we need to generate the UI page as well. Because
        # individually using this method will prompt on developer cmd prompt. Not to user side.
        # So to achieve this we need to render this to html page.
        messages.success(request, 'Profile details updated!')
    return render(request, 'contact.html')
    # return HttpResponse("This is contact page")
