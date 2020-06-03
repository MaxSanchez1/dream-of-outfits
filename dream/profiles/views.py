from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from .models import Profile


class ProfileListView(ListView):
    queryset = Profile.objects.all()


class ProfileDetailView(DetailView):
    model = Profile
