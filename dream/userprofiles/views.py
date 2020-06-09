from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
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
class ProfileView(View, LoginRequiredMixin):
    template_name = "userprofiles/profile_general_list.html"

    def get(self, request, pk=None, *args, **kwargs):
        context = {}
        if pk is not None:
            obj = get_object_or_404(DreamUser, pk=pk)
            context = {
                'object': obj,
                'name': obj.user.first_name + " " +obj.user.last_name,
                'username': obj.user.username,
                'followedby': obj.user_followed_by.all(),
                'following': obj.follows.all(),
            }
        return render(request, self.template_name, context)


class AllProfilesView(ListView, LoginRequiredMixin):
    template_name = 'userprofiles/all_profiles.html'

    def get_queryset(self):
        return DreamUser.objects.all()

