from django.db import models
from django.urls import reverse


class Outfit(models.Model):
    # mandatory
    title = models.CharField(max_length=120)
    top = models.CharField(max_length=120)
    bottom = models.CharField(max_length=120)
    shoes = models.CharField(max_length=120)

    # optional (blank=True)
    jacket = models.CharField(max_length=120, blank=True)
    socks = models.CharField(max_length=120, blank=True)
    hat = models.CharField(max_length=120, blank=True)

    def get_absolute_url(self):
        # self.id is referring to the instance of the object
        return reverse('clothing:outfit-detail', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
