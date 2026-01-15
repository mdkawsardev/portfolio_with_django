from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Contact, AboutSection, ContactEmail, ContactNumber, FooterText, SkillSection, ServiceSection, ClientSection, BannerImage, PortfolioSection, SocialMedia, SkillTitle, ServiceTitle, PortfolioTitle, ClientTitle, ContactTitle, SelfTag
# Create your views here.
def home(request):
    all_info = {
        'Banner_image': BannerImage.objects.all(),
        'Self_tags': SelfTag.objects.all(),
        'Abouts': AboutSection.objects.all(),
        'Skill_title': SkillTitle.objects.all(),
        'Skills': SkillSection.objects.all(),
        'Service_title': ServiceTitle.objects.all(),
        'Services': ServiceSection.objects.all(),
        'Porfolio_title': PortfolioTitle.objects.all(),
        'Porfolios': PortfolioSection.objects.all(),
        'Client_title': ClientTitle.objects.all(),
        'ClientReviews': ClientSection.objects.all(),
        'Contact_title': ContactTitle.objects.all(),
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

def navbar(request):
    if not request.user.is_authenticated:
        return redirect('/loginuser')
    return render(request, 'dashboard/navbar.html')

def banner(request):
    return render(request, 'dashboard/banner.html')

def about(request):
    return render(request, 'dashboard/about.html')
def skill(request):
    return render(request, 'dashboard/skill.html')
def service(request):
    return render(request, 'dashboard/service.html')
def portfolio(request):
    return render(request, 'dashboard/portfolio.html')
def testimonial(request):
    return render(request, 'dashboard/testimonial.html')
def contact(request):
    return render(request, 'dashboard/contact.html')
def footer(request):
    return render(request, 'dashboard/footer.html')

def loginuser(request):
    if request.user.is_authenticated:
        return redirect('/navbar')
    if request.method == "POST":
        userName = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=userName, password=password)
        if user is not None:
            login(request, user)
            return redirect('/navbar')
        else:
            return render(request, 'loginuser.html')
    return render(request, 'loginuser.html')