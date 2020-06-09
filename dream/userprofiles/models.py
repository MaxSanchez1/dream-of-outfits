from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class DreamUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('DreamUser', related_name='user_followed_by', blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('userprofiles:profile', kwargs={"pk": self.pk})


    # this is just for testing at the moment
    # @classmethod
    # def create(cls, user):
    #     dreamuser = cls(user=user)
    #     return dreamuser

# for testing in shell
# from django.contrib.auth.models import User
# from userprofiles.models import DreamUser
