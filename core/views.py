from django.shortcuts import render, reverse
from django.views.generic import CreateView
from .forms import *
# Create your views here.
class SingupView(CreateView):
    template_name = "registration/signup.html"
    form_class = NewUserform
    def get_success_url(self):
        return reverse('home')

def home(request):
    return render(request, 'index.html')