from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
import forms

def index(request):
    return render(request, 'index.html')

def signup(request):
    form = forms.UserForm()
    return render(request, 'signup.html', {'form': form})
