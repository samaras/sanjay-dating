"""datingproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles import views
from django.contrib.auth import views as auth_views

from dating.views import HomeView, AboutUsView, WhatWeDoView, ContactUsView, SignupView, ProfileView, ProfileEditView

urlpatterns = [
	# Static pages:
    url(r'^$', HomeView.as_view(template_name="home.html"), name='home'),
    url(r'^aboutus$', AboutUsView.as_view(template_name="aboutus.html"), name='aboutus'),
    url(r'^whatwedo$', WhatWeDoView.as_view(template_name="whatwedo.html"), name='whatwedo'),
    url(r'^contactus$', ContactUsView.as_view(template_name="contactus.html"), name='contactus'),
    
    # Account pages
    #url(r'^', include('django.contrib.auth.urls')),
    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^change-password/', auth_views.password_change, {'template_name': 'change-password.html'}),
    url(r'^password-reset/', auth_views.password_reset, {'template_name': 'password-reset.html'}),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}),
    url(r'^logout/$', auth_views.logout, name="logout"),

    url(r'^profile/(?P<username>\w+)/$', ProfileView.as_view(), name="user_profile"),
    url(r'^edit-account/(?P<username>\w+)/$', ProfileEditView.as_view(), name="edit_account"),
    
    # Charge user URLs

    # Setup availablity URLs

    # admin 
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', views.serve),
    ]
