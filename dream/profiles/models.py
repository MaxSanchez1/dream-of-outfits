from django.db import models
from django.urls import reverse


# this is a stand-in for when I use the User class and handle authentication but that's a problem for later
class Profile(models.Model):
    # mandatory
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    email = models.CharField(max_length=120)

    def get_absolute_url(self):
        # self.id is referring to the instance of the object
        return reverse('profiles:profile-detail', kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
