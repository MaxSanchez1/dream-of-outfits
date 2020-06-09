from django.urls import path

# import views here once they're added
from .views import (
    ProfileView,
    AllProfilesView,
)


app_name = 'userprofiles'
urlpatterns = [
    path('<int:pk>/', ProfileView.as_view(), name='profile'),
    path('', AllProfilesView.as_view(), name='all-profiles'),
]
