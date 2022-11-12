from django.shortcuts import render, HttpResponse
from .forms import Contact
from django.core.mail import send_mail


def home(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        
        send_mail(
            "message from" + name,
            message,
            email,
            ["derrickokinda9@gmail.com", "developer.derrickokinda9@gmail.com"]
            
        )
    form = Contact
    context = {
        "form":form
    }
    return render(request, "port/home.html", context)

