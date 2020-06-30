from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from pages.views import home_view, about_view, register_view

urlpatterns = [
    path('clothing/', include('clothing.urls')),
    path('userprofiles/', include('userprofiles.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('feed/', include('feed.urls')),
    path('register/', register_view, name='register-view'),
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('about/', about_view, name='about')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
