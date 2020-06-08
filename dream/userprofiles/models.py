from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class DreamUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('DreamUser', related_name='user_followed_by', blank=True)

    def __str__(self):
        return self.user.username
