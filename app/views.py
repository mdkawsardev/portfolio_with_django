from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Contact, AboutSection, ContactEmail, ContactNumber, FooterText, SkillSection, ServiceSection, ClientSection, Banner, PortfolioSection, SocialMedia, SkillTitle, ServiceTitle
# Create your views here.
def home(request):
    all_info = {
        'Banners': Banner.objects.all(),
        'Abouts': AboutSection.objects.all(),
        'Skill_title': SkillTitle.objects.all(),
        'Skills': SkillSection.objects.all(),
        'Service_title': ServiceTitle.objects.all(),
        'Services': ServiceSection.objects.all(),
        'Porfolios': PortfolioSection.objects.all(),
        'ClientReviews': ClientSection.objects.all(),
        'Contacts': Contact.objects.all(),
        'ContactNumbers': ContactNumber.objects.all(),
        'ContactEmails': ContactEmail.objects.all(),
        'SocialMedias': SocialMedia.objects.all(),
        'FooterTexts': FooterText.objects.all()
    }
    return render(request, 'index.html', all_info)

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
        messages.success(request, "Thanks! Your information has been sent.")
    return render(request, 'index.html')
