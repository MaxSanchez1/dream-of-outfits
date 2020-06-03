from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from .models import Outfit
from .forms import OutfitModelForm


class OutfitListView(ListView, LoginRequiredMixin):

    # this is going to be only the outfits that the user has made
    def get_queryset(self):
        return Outfit.objects.filter(creator=self.request.user)



class OutfitDetailView(DetailView):
    model = Outfit
