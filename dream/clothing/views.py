from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    RedirectView,
    TemplateView,
    FormView,
)

from .models import Outfit
from .models import Article
from .models import Collection
from .forms import OutfitModelForm
from .forms import ArticleModelForm
from .forms import CollectionModelForm
from .forms import AddArticleForm
from .forms import AddOutfitForm


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


class CollectionListView(ListView, LoginRequiredMixin):
    template_name = 'clothing/collection_list.html'

    def get_queryset(self):
        return Collection.objects.filter(creator=self.request.user)


class CollectionDetailView(DetailView, LoginRequiredMixin):
    template_name = 'clothing/collection_detail.html'
    model = Collection

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        add_article_form = AddArticleForm(self.request.GET or None)
        add_outfit_form = AddOutfitForm(self.request.GET or None)
        context = self.get_context_data(**kwargs)
        context['add_article_form'] = add_article_form
        context['add_outfit_form'] = add_outfit_form
        return self.render_to_response(context)


class CreateCollectionView(CreateView, LoginRequiredMixin):
    template_name = 'clothing/collection_create_new.html'
    model = Collection
    form_class = CollectionModelForm

    # this is needed so that the form can assign a creator
    def get_form_kwargs(self):
        kwargs = super(CreateCollectionView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class CollectionMainDetailView(TemplateView, LoginRequiredMixin):
    template_name = 'clothing/collection_multiform.html'

    def get(self, request, *args, **kwargs):
        add_article_form = AddArticleForm(self.request.GET or None)
        add_outfit_form = AddOutfitForm(self.request.GET or None)
        context = self.get_context_data(**kwargs)
        context['add_article_form'] = add_article_form
        context['add_outfit_form'] = add_outfit_form
        return self.render_to_response(context)


class AddArticleFormView(FormView, LoginRequiredMixin):
    form_class = AddArticleForm
    template_name = 'clothing/collection_multiform.html'

    # I want this to redirect right back to the detail page of the collection
    def get_success_url(self):
        return reverse_lazy('clothing:collection-detail', kwargs={"pk": self.pk})

    def post(self, request, *args, **kwargs):
        article_form = self.form_class(request.POST)
        outfit_form = AddOutfitForm()
        if article_form.is_valid():
            article_form.save()
            return self.render_to_response(self.get_context_data(success=True))
        else:
            return self.render_to_response(self.get_context_data(article_form=article_form))


class AddOutfitFormView(FormView, LoginRequiredMixin):
    form_class = AddOutfitForm
    template_name = 'clothing/collection_multiform.html'

    # I want this to redirect right back to the detail page of the collection
    def get_success_url(self):
        return reverse_lazy('clothing:collection-detail', kwargs={"pk": self.pk})

    def post(self, request, *args, **kwargs):
        outfit_form = self.form_class(request.POST)
        article_form = AddArticleForm()
        if outfit_form.is_valid():
            outfit_form.save()
            return self.render_to_response(self.get_context_data(success=True))
        else:
            return self.render_to_response(self.get_context_data(outfit_form=outfit_form))

