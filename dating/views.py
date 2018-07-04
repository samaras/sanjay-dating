from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

from django.views.generic import View, UpdateView, DeleteView, CreateView, ListView, TemplateView, DetailView
from django.core.urlresolvers import reverse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

from dating.models import Profile

class HomeView(TemplateView): 
	template_name = "home.html"

class AboutUsView(TemplateView):
	template_name = "about_us.html"

class WhatWeDoView(TemplateView): 
	template_name = "what_we_do.html"

class ContactUsView(TemplateView):
	template_name = "contact_us.html"

class SignupView(CreateView):
	form_class = UserCreationForm
	model = User 
	template_name = "signup.html"

class ProfileView(DetailView):
	model = Profile
	template_name = "profile.html"

class ProfileEditView(UpdateView):
	model = Profile