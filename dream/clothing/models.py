from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Article(models.Model):
    location_choices = (
        ('TOP', 'Top'),
        ('BTM', 'Bottom'),
        ('SHS', 'Shoes'),
    )

    # mandatory
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    actual_location = models.CharField(max_length=60, choices=location_choices, default='None', null=True)
    clothing_type = models.CharField(max_length=60)  # henley, jeans, sneakers
    color = models.CharField(max_length=20)

    # optional
    cut = models.CharField(max_length=60, blank=True)
    pattern = models.CharField(max_length=60, blank=True)
    material = models.CharField(max_length=60, blank=True)

    # experimental liking field
    favorited = models.ManyToManyField(User, blank=True, related_name="article_favorited_by")

    def get_absolute_url(self):
        return reverse('clothing:article-detail', kwargs={"pk": self.pk})

    def __str__(self):
        return "{} {}".format(self.color, self.clothing_type)


class Outfit(models.Model):
    # mandatory
    title = models.CharField(max_length=120)
    top = models.ForeignKey('Article', on_delete=models.SET_NULL, related_name="outfit_top", null=True)
    bottom = models.ForeignKey('Article', on_delete=models.SET_NULL, related_name="outfit_bottom", null=True)
    shoes = models.ForeignKey('Article', on_delete=models.SET_NULL , related_name="outfit_shoes", null=True)

    # # optional (blank=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    # jacket = models.CharField(max_length=120, blank=True)
    # socks = models.CharField(max_length=120, blank=True)
    # hat = models.CharField(max_length=120, blank=True)
    # description = models.TextField(blank=True)
    favorited = models.ManyToManyField(User, blank=True, related_name="outfit_favorited_by")

    def get_absolute_url(self):
        # self.id is referring to the instance of the object
        return reverse('clothing:outfit-detail', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class Collection(models.Model):
    # name of the collection
    name = models.CharField(max_length=120)

    # creator of the collection
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    # articles of clothing in the collection
    articles = models.ManyToManyField('Article', related_name="articles_in_collection")

    # outfits in the collection
    outfits = models.ManyToManyField('Outfit', related_name="outfits_in_collection")

    def get_absolute_url(self):
        return reverse('clothing:collection-detail', kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


