from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.forms import modelform_factory
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

from .forms import *
# Create your views here.
class SingupView(CreateView):
    template_name = "registration/signup.html"
    form_class = NewUserform
    def get_success_url(self):
        return reverse('home')