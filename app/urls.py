from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('Clientcontact', views.Clientcontact, name='Clientcontact'),
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
    path('update/<int:pk>/', views.updateItem, name='update'),
    path('updateimage/<int:pk>/', views.updateimage, name='updateimage'),
    path('insert_updated_image/', views.insert_updated_image, name='insert_updated_image'),
    path('delete/<int:pk>/', views.deleteItem, name='delete'),
    path('insert_updated_data/', views.insert_updated_data, name='insert_updated_data'),
    path('deletecontact/<int:pk>/', views.deleteContacts, name='deletecontact'),
    path('delete_review/<int:pk>/', views.delete_review, name='delete_review'),
    path('insert_data', views.insert_data, name='insert_data'),
    path('delete_portfolio/<int:pk>/', views.delete_portfolio, name='delete_portfolio'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

