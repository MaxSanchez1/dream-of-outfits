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
from .models import Article
from .forms import OutfitModelForm


class OutfitListView(ListView, LoginRequiredMixin):
    # this is going to be only the outfits that the user has made
    def get_queryset(self):
        return Outfit.objects.filter(creator=self.request.user)


class OutfitDetailView(DetailView, LoginRequiredMixin):
    model = Outfit


class FavoritedOutfitListView(ListView, LoginRequiredMixin):
    template_name = 'clothing/favorited_outfit_list.html'

    # using related_names to get that query of outfits that the user has favorited
    def get_queryset(self):
        return self.request.user.outfit_favorited_by.all()


class ArticleListView(ListView, LoginRequiredMixin):
    def get_queryset(self):
        return Article.objects.filter(creator=self.request.user)


class ArticleDetailView(DetailView, LoginRequiredMixin):
    model = Article


class FavoritedArticleListView(ListView, LoginRequiredMixin):
    template_name = 'clothing/favorited_article_list.html'

    # using related_names to get that query of outfits that the user has favorited
    def get_queryset(self):
        return self.request.user.article_favorited_by.all()



