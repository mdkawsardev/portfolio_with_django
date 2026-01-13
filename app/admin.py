from django.contrib import admin
from .models import Contact, Banner, SkillSection, AboutSection, ServiceSection
# Register your models here.
admin.site.register(Banner)
admin.site.register(SkillSection)
@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(ServiceSection)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']