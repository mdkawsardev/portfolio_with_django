from django.db import models

# Create your models here.
class Banner(models.Model):
    image = models.ImageField(default='example.png', blank=True, upload_to='media')
    sideTitle = models.CharField(max_length=255)
    mainTitle = models.CharField(max_length=255)

class AboutSection(models.Model):
    title = models.CharField(max_length=50)
    greeting = models.CharField(max_length=255, default='Hello')
    description = models.TextField()
    profile_image = models.ImageField(default='example.png', blank=True, upload_to='media')
    profile_text = models.TextField()
    btn1 = models.CharField(max_length=50)
    btn1_Link = models.TextField()
    btn2 = models.CharField(max_length=255)
    btn2_Link = models.TextField()
    point1_number = models.CharField(max_length=50)
    point1_text = models.CharField(max_length=100)
    point2_number = models.CharField(max_length=50)
    point2_text = models.CharField(max_length=100)
    point3_number = models.CharField(max_length=50)
    point3_text = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class SkillTitle(models.Model):
    title = models.CharField(max_length=50)

class SkillSection(models.Model):
    range_text = models.CharField(max_length=100)
    range_percentage = models.CharField(max_length=10)

class ServiceTitle(models.Model):
    title = models.CharField(max_length=100)

class ServiceSection(models.Model):
    service_icon = models.CharField(max_length=255)
    service_name = models.CharField(max_length=255)
    service_description = models.TextField()

class PortfolioTitle(models.Model):
    title = models.CharField(max_length=100)

class PortfolioSection(models.Model):
    filter_keyword = models.CharField(max_length=100)
    project_url = models.CharField(max_length=255)
    project_image = models.ImageField(upload_to='media', blank=True)

class ClientSection(models.Model):
    title = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    client_profession = models.CharField(max_length=100)
    client_comments = models.TextField()
    client_photo = models.ImageField(blank=True, upload_to='media', default='default.png')


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)

class ContactNumber(models.Model):
    number = models.CharField(max_length=50)
    def __str__(self):
        return self.number
    
class ContactEmail(models.Model):
    email = models.EmailField(max_length=50)
    def __str__(self):
        return self.email

class SocialMedia(models.Model):
    icon = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

class FooterText(models.Model):
    footer_texts = models.TextField()
    def __str__(self):
        return self.footer_texts