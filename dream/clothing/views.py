from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    RedirectView,
)

from .models import Outfit
from .models import Article
from .forms import OutfitModelForm
from .forms import ArticleModelForm


class OutfitListView(ListView, LoginRequiredMixin):
    # this is going to be only the outfits that the user has made
    def get_queryset(self):
        return Outfit.objects.filter(creator=self.request.user)


class OutfitDetailView(DetailView, LoginRequiredMixin):
    model = Outfit

    def get_context_data(self, **kwargs):
        obj = get_object_or_404(Outfit, pk=self.kwargs.get('pk'))
        context = super().get_context_data(**kwargs)
        context['is_favorited'] = self.request.user in obj.favorited.all()
        return context


class OutfitFavoriteToggle(RedirectView, LoginRequiredMixin):
    def get_redirect_url(self, *args, **kwargs):
        obj = get_object_or_404(Outfit, pk=self.kwargs.get('pk'))
        url_ = obj.get_absolute_url()
        user = self.request.user
        # make this user like this article
        if user in obj.favorited.all():
            obj.favorited.remove(user)
        else:
            obj.favorited.add(user)
        return url_


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

    def get_context_data(self, **kwargs):
        obj = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        context = super().get_context_data(**kwargs)
        context['is_favorited'] = self.request.user in obj.favorited.all()
        return context


class ArticleFavoriteToggle(RedirectView, LoginRequiredMixin):
    def get_redirect_url(self, *args, **kwargs):
        obj = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        url_ = obj.get_absolute_url()
        user = self.request.user
        # make this user like this article
        if user in obj.favorited.all():
            obj.favorited.remove(user)
        else:
            obj.favorited.add(user)
        return url_


class FavoritedArticleListView(ListView, LoginRequiredMixin):
    template_name = 'clothing/favorited_article_list.html'

    # using related_names to get that query of outfits that the user has favorited
    def get_queryset(self):
        return self.request.user.article_favorited_by.all()


class CreateOutfitView(CreateView, LoginRequiredMixin):
    template_name = 'clothing/create_new_outfit.html'
    model = Outfit
    form_class = OutfitModelForm

    # this is needed so that the form can assign a creator
    def get_form_kwargs(self):
        kwargs = super(CreateOutfitView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class CreateArticleView(CreateView, LoginRequiredMixin):
    template_name = 'clothing/create_new_article.html'
    model = Article
    form_class = ArticleModelForm

    # this is needed so that the form can assign a creator
    def get_form_kwargs(self):
        kwargs = super(CreateArticleView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs



