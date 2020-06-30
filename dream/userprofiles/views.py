from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic.base import View
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    RedirectView,
)

from .models import DreamUser
from clothing.models import Outfit
from clothing.models import Article
from clothing.models import Collection

# Create your views here.
# TODO
# user profile general view
# should be eventually customizable enough to have "add outfit" links and stuff to your own but not when you're
# looking at others'
# follower view
# following view


# Profile information: Photo (text placeholder for now), basic info (can get from User), following #, followed #
# future things to add: featured outfits
# this is the arbitrary profile view, not the one that you see exactly for your own
class ProfileView(View, LoginRequiredMixin):
    template_name = "userprofiles/profile_general_list.html"

    def get(self, request, pk=None, *args, **kwargs):
        context = {}
        if pk is not None:
            obj = get_object_or_404(DreamUser, pk=pk)
            context = {
                'object': obj,
                'name': obj.user.first_name + " " + obj.user.last_name,
                'username': obj.user.username,
                'followedby': len(obj.user_followed_by.all()),
                'following': len(obj.follows.all()),
            }
        your_dream_account = get_object_or_404(DreamUser, user=self.request.user)
        dream_user_of_current_page = get_object_or_404(DreamUser, pk=pk)
        context['is_following'] = dream_user_of_current_page in your_dream_account.follows.all()
        return render(request, self.template_name, context)


class AllProfilesView(ListView, LoginRequiredMixin):
    template_name = 'userprofiles/all_profiles.html'

    # this is a searchable queryset
    # something to add could be only showing the top (5/10) most followed users by default
    # for now it shows all of them
    # when you search for users, it comes up with ones that match with your search
    def get_queryset(self):
        return_queryset = DreamUser.objects.all()  # eventually change this since there will be too many
        try:
            query = self.request.GET["q"]
        except KeyError:
            return return_queryset
        # "if query" will be false if there is no query yet
        if query:
            return_queryset = return_queryset.filter(user__username__icontains=query)
        # else is going to do nothing for the moment which will keep the filter at ...all()
        return return_queryset


class FollowAProfileToggle(RedirectView, LoginRequiredMixin):
    def get_redirect_url(self, pk=None, *args, **kwargs):
        dream_user_of_current_page = get_object_or_404(DreamUser, pk=pk)
        url_ = dream_user_of_current_page.get_absolute_url()
        your_dream_account = get_object_or_404(DreamUser, user=self.request.user)
        # make this user like this article
        if dream_user_of_current_page in your_dream_account.follows.all():
            your_dream_account.follows.remove(dream_user_of_current_page)
        else:
            your_dream_account.follows.add(dream_user_of_current_page)
        return url_


class PersonalProfileView(View, LoginRequiredMixin):
    template_name = "userprofiles/personal_profile.html"

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(DreamUser, user=self.request.user)
        context = {
            'object': obj,
            'name': obj.user.first_name + " " + obj.user.last_name,
            'username': obj.user.username,
            'followedby': len(obj.user_followed_by.all()),
            'following': len(obj.follows.all()),
            'image_source': obj.image.url
        }
        return render(request, self.template_name, context)


# uses self.request.user because this is the PERSONAL following page
class PersonalFollowingListView(ListView, LoginRequiredMixin):
    template_name = "userprofiles/i_am_following_list.html"

    def get_queryset(self):
        user_ = self.request.user
        this_user = get_object_or_404(DreamUser, user=self.request.user)
        return this_user.follows.all()


# uses self.request.user because this is the PERSONAL following page
class PersonalFollowedByListView(ListView, LoginRequiredMixin):
    template_name = "userprofiles/i_am_followed_by_list.html"

    def get_queryset(self):
        user_ = self.request.user
        this_user = get_object_or_404(DreamUser, user=self.request.user)
        return this_user.user_followed_by.all()


class GeneralFollowingListView(ListView, LoginRequiredMixin):
    template_name = "userprofiles/general_is_following_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        dream_user = get_object_or_404(DreamUser, pk=self.kwargs.get('pk'))
        context = super().get_context_data(**kwargs)
        context['u_name'] = dream_user.user.username
        return context

    def get_queryset(self):
        dream_user = get_object_or_404(DreamUser, pk=self.kwargs.get('pk'))
        return dream_user.follows.all()


# I can abstract this view and the above view and then override get_queryset
class GeneralFollowedByListView(ListView, LoginRequiredMixin):
    template_name = "userprofiles/general_is_followed_by_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        dream_user = get_object_or_404(DreamUser, pk=self.kwargs.get('pk'))
        context = super().get_context_data(**kwargs)
        context['u_name'] = dream_user.user.username
        return context

    def get_queryset(self):
        dream_user = get_object_or_404(DreamUser, pk=self.kwargs.get('pk'))
        return dream_user.user_followed_by.all()


# allow users to see the outfits of others. should be accessible from profile views of other people
class OtherOutfitListView(ListView, LoginRequiredMixin):
    template_name = "userprofiles/someone_elses_outfits.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        dream_user = get_object_or_404(DreamUser, pk=self.kwargs.get('pk'))
        context = super().get_context_data(**kwargs)
        context['u_name'] = dream_user.user.username
        return context

    def get_queryset(self):
        dream_user = get_object_or_404(DreamUser, pk=self.kwargs.get('pk'))
        return Outfit.objects.filter(creator=dream_user.user)


# allow users to see the articles of others. should be accessible from profile views of other people
class OtherArticleListView(ListView, LoginRequiredMixin):
    template_name = "userprofiles/someone_elses_articles.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        dream_user = get_object_or_404(DreamUser, pk=self.kwargs.get('pk'))
        context = super().get_context_data(**kwargs)
        context['u_name'] = dream_user.user.username
        return context

    def get_queryset(self):
        dream_user = get_object_or_404(DreamUser, pk=self.kwargs.get('pk'))
        return Article.objects.filter(creator=dream_user.user)


# allow users to see the articles of others. should be accessible from profile views of other people
class OtherCollectionListView(ListView, LoginRequiredMixin):
    template_name = "userprofiles/someone_elses_collections.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        dream_user = get_object_or_404(DreamUser, pk=self.kwargs.get('pk'))
        context = super().get_context_data(**kwargs)
        context['u_name'] = dream_user.user.username
        return context

    def get_queryset(self):
        dream_user = get_object_or_404(DreamUser, pk=self.kwargs.get('pk'))
        return Collection.objects.filter(creator=dream_user.user)




