from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Contact, AboutSection, ContactEmail, ContactNumber, FooterText, SkillSection, ServiceSection, ClientSection, BannerImage, PortfolioSection, SocialMedia, SkillTitle, ServiceTitle, PortfolioTitle, ClientTitle, ContactTitle, SelfTag


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
        'ClientReviews': ClientSection.objects.all().order_by('-id'),
        'Contact_title': ContactTitle.objects.all(),
        'Contacts': Contact.objects.all(),
        'ContactNumbers': ContactNumber.objects.all(),
        'ContactEmails': ContactEmail.objects.all(),
        'SocialMedias': SocialMedia.objects.all(),
        'FooterTexts': FooterText.objects.all()
    }
    if request.method == "POST":
        userName = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=userName, password=password)
        if user is not None:
            login(request, user)
            return redirect('/navbar')
        else:
            return render(request, 'loginuser.html')
    return render(request, 'index.html', all_info)


def Clientcontact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        Contact.objects.create(
            name=name,
            email=email,
            phone=phone
        )
        messages.success(request, "Thanks! Your information has been sent.")
    return redirect('/')


def navbar(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'dashboard/navbar.html')


def banner(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        banner_data = {
        'banner_tag': SelfTag.objects.all(),
        'banner_img': BannerImage.objects.all()
        }
        if request.method == "POST":
            image = request.FILES.get('image')
            BannerImage.objects.create(
                image=image
            )
            messages.success(request, "Image uploaded successfully!")
            return redirect('/banner')
        if request.method == "POST":
            banner_tag = request.POST.get('title_name')
            SelfTag.objects.create(self_tags=banner_tag)
            messages.success(request, "Tag added successfully!")
        return render(request, 'dashboard/banner.html', banner_data)


def about(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'dashboard/about.html')


def skill(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'dashboard/skill.html')


def service(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'dashboard/service.html')


def portfolio(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'dashboard/portfolio.html')


def testimonial(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            clinet_name = request.POST['name']
            client_tag = request.POST['t_name']
            comments = request.POST['comments']
            client_image = request.FILES['c_im']
            ClientSection.objects.create(
                client_name=clinet_name,
                client_profession=client_tag,
                client_comments=comments,
                client_photo=client_image
            )
            messages.success(request, 'New client added')
        context = {
            'information': ClientSection.objects.all().order_by('-id')
        }
        return render(request, 'dashboard/testimonial.html', context)


def contact(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        context = {
            'contacts': Contact.objects.all()
        }
        return render(request, 'dashboard/contact.html', context)


def footer(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'dashboard/footer.html')


def loginuser(request):
    if request.user.is_authenticated:
        return redirect('/navbar')
    return render(request, 'index.html')


def logoutuser(request):
    logout(request)
    return redirect('/')


def updateItem(request, pk):
    update_data = {
        'update': SelfTag.objects.filter(id=pk).all()
    }
    return render(request, 'update.html', update_data)

def updateimage(request, pk):
    update_img = {
        'update': BannerImage.objects.filter(id=pk).all()
    }
    return render(request, 'updateimage.html', update_img)

def insert_updated_image(request):
    pass
    # messages.success(request, 'Image has been updated successfully!')
    # return redirect('/banner')

def deleteItem(request, pk):
        delete_tag = SelfTag.objects.filter(id=pk)
        delete_tag.delete()
        messages.success(request, "Tag deleted successfully!")
        return redirect('/banner')

def deleteContacts(request, pk):
    deleteContact = Contact.objects.filter(id=pk)
    deleteContact.delete()
    messages.success(request, 'Client information has deleted successfully!')
    return redirect('contact')


def insert_updated_data(request):
    if request.method == "POST":
        id = request.POST.get('id')
        tag_name = request.POST.get('tag_name')
        selected_data = SelfTag.objects.filter(id=id)
        selected_data.update(self_tags=tag_name)
        messages.success(request, "Tag updated successfully!")
        return redirect('/banner')
    
def delete_review(request, pk):
    find = ClientSection.objects.filter(id=pk)
    find.delete()
    return redirect('/testimonial')