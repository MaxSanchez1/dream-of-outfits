from django.urls import path

from .views import FeedView


app_name = 'feed'
urlpatterns = [
    path('', FeedView.as_view(), name='feed-view'),
]
