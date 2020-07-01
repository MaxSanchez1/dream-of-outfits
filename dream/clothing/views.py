from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.forms.widgets import CheckboxSelectMultiple
from django.forms.models import modelform_factory
from django import forms
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    RedirectView,
    TemplateView,
    FormView,
    View,
)

from .models import Outfit
from .models import Article
from .models import Collection
from userprofiles.models import DreamUser
from .forms import OutfitModelForm
from .forms import ArticleModelForm
from .forms import CollectionModelForm
from .forms import CollectionUpdateForm
# from .forms import AddArticleForm
# from .forms import AddOutfitForm


# helper to get default article image when there is none uploaded
def get_default_image(user_obj):
    try:
        return_url = user_obj.image.url
        return return_url
    # catches when there's no image assigned
    except ValueError:
        return "/media/default-any/base_default.JPG"


class OutfitListView(ListView, LoginRequiredMixin):
    # this is going to be only the outfits that the user has made
    def get_queryset(self):
        return Outfit.objects.filter(creator=self.request.user)


class OutfitDetailView(DetailView, LoginRequiredMixin):
    model = Outfit

    def get_context_data(self, **kwargs):
        obj = get_object_or_404(Outfit, pk=self.kwargs.get('pk'))
        # print(obj.creator)
        dream_user_of_creator = get_object_or_404(DreamUser, user=obj.creator)
        context = super().get_context_data(**kwargs)
        context['is_favorited'] = self.request.user in obj.favorited.all()
        context['creator_acc'] = dream_user_of_creator
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
        dream_user_of_creator = get_object_or_404(DreamUser, user=obj.creator)
        context = super().get_context_data(**kwargs)
        context['image_source'] = get_default_image(obj)
        context['is_favorited'] = self.request.user in obj.favorited.all()
        context['creator_acc'] = dream_user_of_creator
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


class CollectionListView(ListView, LoginRequiredMixin):
    template_name = 'clothing/collection_list.html'

    def get_queryset(self):
        return Collection.objects.filter(creator=self.request.user)


# this page has two forms on it, one adds to Article, one adds to Outfit
class CollectionDetailView(DetailView, LoginRequiredMixin):
    template_name = 'clothing/collection_detail.html'
    model = Collection

    def get_context_data(self, *, object_list=None, **kwargs):
        # add_article_form = AddArticleForm(self.request.GET or None)
        # add_outfit_form = AddOutfitForm(self.request.GET or None)
        context = super().get_context_data(**kwargs)
        # context['add_article_form'] = add_article_form
        # context['add_outfit_form'] = add_outfit_form
        instance_ = get_object_or_404(Collection, pk=self.kwargs.get('pk'))
        context['can_edit'] = str(self.request.user) == str(instance_.creator)
        return context

    # def post(self, request, *args, **kwargs):
    #     instance_ = get_object_or_404(Collection, pk=self.kwargs.get('pk'))
    #     article_form = AddArticleForm(request.POST or None, instance=instance_)
    #     outfit_form = AddOutfitForm(request.POST or None, instance=instance_)
    #     if article_form.is_valid():
    #         article_form.save()
    #         return HttpResponseRedirect(self.request.path_info)
    #     elif outfit_form.is_valid():
    #         outfit_form.save()
    #         return HttpResponseRedirect(self.request.path_info)
    #     else:
    #         return HttpResponseRedirect(self.request.path_info)


class CreateCollectionView(CreateView, LoginRequiredMixin):
    template_name = 'clothing/collection_create_new.html'
    model = Collection
    form_class = CollectionModelForm

    # this is needed so that the form can assign a creator
    def get_form_kwargs(self):
        kwargs = super(CreateCollectionView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class CollectionUpdateView(UpdateView, LoginRequiredMixin):
    model = Collection
    form_class = CollectionUpdateForm
    template_name = 'clothing/collection_update_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['articles'] = Article.objects.filter(creator=self.request.user)
        kwargs['outfits'] = Outfit.objects.filter(creator=self.request.user)
        return kwargs

