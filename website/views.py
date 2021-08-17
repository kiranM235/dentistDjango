from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
        return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def patients(request):
    return render(request, 'patients.html', {})

def news(request):
    return render(request, 'news.html', {})

def services(request):
    return render(request, 'services.html', {})

def contact(request):
    if request.method == "POST":
        message_fullname = request.POST['message-fullname']
        #lname = request.POST['lname']
        #date = request.POST['date']
        message_email = request.POST['message-email']
        message = request.POST['message']
        #note = request.POST['note']

        # send an email
        send_mail(
            'message_fullname', # subject
            message, # message
            message_email, # from email
            ['kiranmaharjan1989@gmail.com'], # To Email

        )    
        return render(request, 'contact.html', {'message_fullname': message_fullname})
    
    else: 
        return render(request, 'contact.html', {})




