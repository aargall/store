from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('welcome.html', views.index, name='welcome'),
    path('about', views.about, name='about'),
    path('about', views.about, name='about'),
    path('gallery', views.gallery, name='gallery'),
    path('contact', views.contact, name='contact'),
    path('manage', views.model_form_upload, name='manage')
]
#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]