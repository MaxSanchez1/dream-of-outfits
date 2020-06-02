from django.db import models
from django.urls import reverse

import datetime


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    date = models.DateField(default=datetime.date.today())
    content = models.TextField()

    # add a get absolute url method here once we hook it up to the url
    def get_absolute_url(self):
        # self.id is referring to the instance of the object
        return reverse('blog:article-detail', kwargs={"id": self.id})
