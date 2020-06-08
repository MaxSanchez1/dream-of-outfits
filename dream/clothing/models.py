from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Article(models.Model):
    # mandatory
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    clothing_type = models.CharField(max_length=60)  # pants, shirt, dress
    color = models.CharField(max_length=20)

    # optional
    cut = models.CharField(max_length=60, blank=True)
    pattern = models.CharField(max_length=60, blank=True)
    material = models.CharField(max_length=60, blank=True)

    # experimental liking field
    favorited_by = models.ManyToManyField(User, blank=True, related_name="article_favorited_by")

    def get_absolute_url(self):
        return reverse('clothing:article-detail', kwargs={"pk": self.pk})

    def __str__(self):
        return "{} {}".format(self.color, self.clothing_type)


class Outfit(models.Model):
    # mandatory
    title = models.CharField(max_length=120)
    top = models.ManyToManyField('Article', related_name="outfit_top")
    bottom = models.ManyToManyField('Article', related_name="outfit_bottom")
    shoes = models.ManyToManyField('Article', related_name="outfit_shoes")

    # below just commented out for simplicity's sake while I figure out how this database is structured
    # # optional (blank=True)
    # creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # # creation_date = models.DateTimeField(auto_now_add=True)
    # jacket = models.CharField(max_length=120, blank=True)
    # socks = models.CharField(max_length=120, blank=True)
    # hat = models.CharField(max_length=120, blank=True)
    # description = models.TextField(blank=True)
    favorited_by = models.ManyToManyField(User, blank=True, related_name="outfit_favorited_by")

    def get_absolute_url(self):
        # self.id is referring to the instance of the object
        return reverse('clothing:outfit-detail', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


