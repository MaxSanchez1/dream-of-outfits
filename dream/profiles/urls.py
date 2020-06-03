from django.urls import path

# import views here once they're added
from .views import (
    ProfileDetailView,
    ProfileListView,
)


app_name = 'profiles'
urlpatterns = [
    path('', ProfileListView.as_view(), name='profile-list'),
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
]
