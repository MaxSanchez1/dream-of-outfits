from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from clothing.models import Outfit
from userprofiles.models import DreamUser


# feed going to be a list of outfits, sorted by most recently created
class FeedView(ListView, LoginRequiredMixin):
    template_name = "feed/recent_feed_list.html"

    # outfits of the people the user follows
    def get_queryset(self):
        # getting the list of people the user follows
        this_user = get_object_or_404(DreamUser, user=self.request.user)
        people_this_user_follows = this_user.follows.all()
        # now we have to get a list of all of their outfits
        outfit_pks = []
        # iterate through people adding their outfits to the list of id's we're gonna show
        for person in people_this_user_follows:
            # note: person is a DreamUser
            # filter outfits by creator=person
            for outfit in Outfit.objects.filter(creator=person.user):
                # preventing duplicates if that somehow happens
                if outfit.id not in outfit_pks:
                    outfit_pks.append(outfit.id)
        return Outfit.objects.filter(pk__in=outfit_pks).order_by('-creation_date')

