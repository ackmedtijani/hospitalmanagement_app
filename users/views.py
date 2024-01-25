from django.shortcuts import render
from django.views.generic import CreateView


from allauth.account.views import SignupView

from .forms import MyCustomSignupForm


class RegisterView(SignupView):

    form_class = MyCustomSignupForm

# Create your views here.
