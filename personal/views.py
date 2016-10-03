from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from forms import UserForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf



def index(request):
    return render(request, 'personal/home.html')


def create(request):
    form = UserForm()
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/success')
    return render(request, "personal/Register.html", {
        'form': form,
    })
