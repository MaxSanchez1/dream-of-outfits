from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
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

    def get_queryset(self):
        return DreamUser.objects.all()


class FollowAProfileToggle(RedirectView, LoginRequiredMixin):
    def get_redirect_url(self, pk=None, *args, **kwargs):
        dream_user_of_current_page = get_object_or_404(DreamUser, pk=pk)
        # this is hardcoded for now, find out how to link back to referrer maybe
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

