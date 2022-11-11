from django.shortcuts import render, HttpResponse
from .forms import Contact


def home(request):
    form = Contact
    context = {
        "form":form
    }
    return render(request, "port/home.html", context)

def contact(request):
   
    form = Contact
    context ={
        "form":form
    }
    
    return render (request, "port/contact.html", context)