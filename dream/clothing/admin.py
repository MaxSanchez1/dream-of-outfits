from django.contrib import admin

# Register your models here.
from .models import Outfit, Article

admin.site.register(Outfit)
admin.site.register(Article)
