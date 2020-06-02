from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from .models import Outfit
from .forms import OutfitModelForm


class OutfitListView(ListView):
    # this will eventually be "all outfits that the user has made" but for now it's just gonna be all of them
    queryset = Outfit.objects.all()


class OutfitDetailView(DetailView):
    model = Outfit
