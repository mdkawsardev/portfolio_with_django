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
            messages.success(request, f"Welcome, {userName}. You've logged in")
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
        if request.method == "POST":
            about_title = request.POST['about_title']
            greeting = request.POST['greeting']
            details = request.POST['details']
            profile_text = request.POST['profile_text']
            btn1Text = request.POST['btn1Text']
            btn2Text = request.POST['btn2Text']
            btn1Link = request.POST['btn1Link']
            btn2Link = request.POST['btn2Link']
            countDownText1 = request.POST['countDownText1']
            countDownText2 = request.POST['countDownText2']
            countDownText3 = request.POST['countDownText3']
            count1Down = request.POST['count1Down']
            count2Down = request.POST['count2Down']
            count3Down = request.POST['count3Down']
            profile = request.FILES['profile']
            AboutSection.objects.update(
                title=about_title,
                greeting=greeting,
                description=details,
                profile_image=profile,
                profile_text=profile_text,
                btn1=btn1Text,
                btn1_Link=btn1Link,
                btn2=btn2Text,
                btn2_Link=btn2Link,
                point1_number=count1Down,
                point1_text=countDownText1,
                point2_number=count2Down,
                point2_text=countDownText2,
                point3_number=count3Down,
                point3_text=countDownText3
            )
            messages.success(request, "All Information have been updated!")
        context = {
            'all_data': AboutSection.objects.all()
        }
        return render(request, 'dashboard/about.html', context)


def skill(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        context = {
            'all_data': SkillSection.objects.all()
        }
        return render(request, 'dashboard/skill.html', context)


def service(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        context = {
            'all_data': ServiceSection.objects.all()
        }
        return render(request, 'dashboard/service.html', context)


def portfolio(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        context = {
            'all_data': PortfolioSection.objects.all()
        }
        return render(request, 'dashboard/portfolio.html', context)


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
    messages.success(request, "You've logged out")
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
    delete_client = find.delete()
    if delete_client:
        messages.success(request, 'Client removed!')
    return redirect('/testimonial')

def insert_data(request):
    if request.method == "POST":
        category = request.POST['category']
        category_image = request.FILES['c_image']
        category_link = request.POST['link']
        PortfolioSection.objects.create(
            filter_keyword=category,
            project_url=category_link,
            project_image=category_image
        )
        messages.success(request, 'New category added successfully!')
    return redirect('/portfolio')

def update_portfolio_title(request):
    if request.method == "POST":
        portfolio_title = request.POST['portfolio_title']
        PortfolioTitle.objects.update(
            title=portfolio_title
        )
        messages.success(request, "Title updated successfully!")
    return redirect('/portfolio')

def delete_portfolio(request, pk):
    get_item = PortfolioSection.objects.filter(id=pk)
    remove = get_item.delete()
    if remove:
        messages.success(request, 'Category deleted successfully!')
        return redirect('/portfolio')
    
def delete_service(request, pk):
    get_item = ServiceSection.objects.filter(id=pk)
    remove = get_item.delete()
    if remove:
        messages.success(request, 'Service deleted successfully!')
        return redirect('/service')
    
def add_services(request):
    if request.method == "POST":
        service_icon = request.POST['s_icon']
        service_name = request.POST['s_name']
        service_desc = request.POST['details']
        ServiceSection.objects.create(
            service_icon=service_icon,
            service_name=service_name,
            service_description=service_desc
        )
        messages.success(request, 'Service added successfully!')
    return redirect('/service')

def add_services_title(request):
    if request.method == "POST":
        service_title = request.POST['s_title']
        ServiceTitle.objects.update(
            title=service_title
        )
        messages.success(request, 'Service title updated successfully!')
    return redirect('/service')

def add_skills(request):
    if request.method == "POST":
        range_text = request.POST['s_name']
        range_percentage = request.POST['percent']
        SkillSection.objects.create(
            range_text=range_text,
            range_percentage=range_percentage
        )
        messages.success(request, "New skill has been added successfully!")
    return redirect('/skill')

def update_skill_title(request):
    if request.method == "POST":
        title = request.POST['skill_title']
        SkillTitle.objects.update(
            title=title
        )
        messages.success(request, "Title updated successfully!")
    return redirect('/skill')

def delete_skill(request, pk):
    get_item = SkillSection.objects.filter(id=pk)
    remove = get_item.delete()
    if remove:
        messages.success(request, 'Skill deleted successfully!')
        return redirect('/skill')