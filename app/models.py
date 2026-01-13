from django.db import models

# Create your models here.
class Banner(models.Model):
    image = models.ImageField(default='example.png', blank=True, upload_to='media')
    sideTitle = models.CharField(max_length=255)
    mainTitle = models.CharField(max_length=255)
class AboutSection(models.Model):
    title = models.CharField(max_length=50)
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
    
class SkillSection(models.Model):
    title = models.CharField(max_length=50)
    range_text = models.CharField(max_length=100)
    range_percentage = models.CharField(max_length=10)

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    def __str__(self):
        return self.name