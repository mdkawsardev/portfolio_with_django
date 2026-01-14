from django.contrib import admin
from django import forms
from .models import Contact, Banner, SkillSection, AboutSection, ServiceSection, PortfolioSection, ClientSection, SocialMedia, ContactNumber, ContactEmail, FooterText, SkillTitle, ServiceTitle
# Register your models here.
admin.site.register(Banner)
admin.site.register(SkillSection)
admin.site.register(ClientSection)
admin.site.register(SocialMedia)
admin.site.register(ContactNumber)
admin.site.register(ContactEmail)
admin.site.register(FooterText)
admin.site.register(SkillTitle)
admin.site.register(ServiceTitle)
@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(ServiceSection)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']

# This is for placeholder in admin input
class PortfolioSectionForm(forms.ModelForm):
    class Meta:
        model = PortfolioSection
        fields = ['title','filter_keyword', 'project_url', 'project_image']
        widgets = {
            'filter_keyword': forms.TextInput(attrs={
                'placeholder': 'frontend, backend, wordpress, etc.'
            }),
            'project_url': forms.URLInput(attrs={
                'placeholder': 'https://myproject.com'
            }),
        }

class PortfolioSectionAdmin(admin.ModelAdmin):
    form = PortfolioSectionForm

admin.site.register(PortfolioSection, PortfolioSectionAdmin)