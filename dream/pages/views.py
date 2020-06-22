from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserCreationFormWithName
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from userprofiles.models import DreamUser


# Create your views here.
def home_view(request, *args, **kwargs):
    # return render(request, 'home.html', {})
    return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
    # return render(request, 'home.html', {})
    return render(request, "about.html", {})


def register_view(request, *args, **kwargs):
    if request.method == "POST":
        form = UserCreationFormWithName(request.POST)
        if form.is_valid():
            user = form.save()
            # creating a new dream user here
            new_guy = DreamUser.create(user)
            DreamUser.save(new_guy)
            login(request, user)
            # this is just the default homepage for now
            return redirect('/clothing')
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
            return render(request, 'registration/register.html', context={"form": form})
    form = UserCreationFormWithName
    return render(request, 'registration/register.html', context={"form": form})
