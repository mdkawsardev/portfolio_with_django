from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Contact
# Create your views here.
def home(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        Contact.objects.create(
            name = name,
            email = email,
            phone = phone
        )
        messages.success(request, "Thanks! Your info has been sent.")
    return render(request, 'index.html')
