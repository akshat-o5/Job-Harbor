from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Contact

# Create your views here.

def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        if len(name) < 2 or len(email) < 3 or len(phone) < 9 or len(desc) < 2:
            error_message = "Please fill the form correctly"
        else:
            contact = Contact(name=name, email=email, phone=phone, desc=desc)
            contact.save()
            success_message = "Your message has been successfully submitted!"

    return render(request, 'home/contact.html', locals())




def pp(request):
    return render(request, 'home/pp.html')    


def tnc(request):
    return render(request, 'home/tnc.html')    