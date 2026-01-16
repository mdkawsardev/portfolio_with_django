from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('navbar/', views.navbar, name='navbar'),
    path('banner/', views.banner, name='banner'),
    path('about/', views.about, name='about'),
    path('skill/', views.skill, name='skill'),
    path('service/', views.service, name='service'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('contact/', views.contact, name='contact'),
    path('footer/', views.footer, name='footer'),
    path('logout/', views.logoutuser, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

