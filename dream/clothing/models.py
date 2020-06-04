from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# this may eventually become just holding article models, but for now it's just text
class Outfit(models.Model):
    # mandatory
    title = models.CharField(max_length=120)
    top = models.CharField(max_length=120)
    bottom = models.CharField(max_length=120)
    shoes = models.CharField(max_length=120)

    # optional (blank=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # creation_date = models.DateTimeField(auto_now_add=True)
    jacket = models.CharField(max_length=120, blank=True)
    socks = models.CharField(max_length=120, blank=True)
    hat = models.CharField(max_length=120, blank=True)

    def get_absolute_url(self):
        # self.id is referring to the instance of the object
        return reverse('clothing:outfit-detail', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class Article(models.Model):
    # mandatory
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # user who made this
    type = models.CharField(max_length=60)  # jeans, tee, dress etc...
    color = models.CharField(max_length=20)

    # optional
    cut = models.CharField(max_length=60)
    pattern = models.CharField(max_length=60)
    texture = models.CharField(max_length=60)
    brand_example = models.CharField(max_length=60)
    link_example = models.CharField(max_length=60)
    cost_of_example = models.FloatField()

    def get_absolute_url(self):
        return reverse('clothing:article-detail', kwargs={"pk": self.pk})

    def __str__(self):
        return "%s %s".format(self.color, self.type)


