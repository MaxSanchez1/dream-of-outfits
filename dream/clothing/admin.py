from django.contrib import admin

# Register your models here.
from .models import Outfit, Article, Collection

admin.site.register(Outfit)
admin.site.register(Article)
admin.site.register(Collection)
