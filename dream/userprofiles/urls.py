from django.urls import path

# import views here once they're added
from .views import (
    ProfileView,
    AllProfilesView,
    PersonalProfileView,
    PersonalFollowingListView,
    PersonalFollowedByListView,
    GeneralFollowingListView,
    GeneralFollowedByListView,
)


app_name = 'userprofiles'
urlpatterns = [
    path('', AllProfilesView.as_view(), name='all-profiles'),  # just for debugging, only for staff
    path('my-profile/', PersonalProfileView.as_view(), name='my-profile'),
    path('my-profile/following/', PersonalFollowingListView.as_view(), name='i-am-following'),
    path('my-profile/followed-by/', PersonalFollowedByListView.as_view(), name='i-am-followed-by'),
    path('<int:pk>/', ProfileView.as_view(), name='profile'),
    path('<int:pk>/following/', GeneralFollowingListView.as_view(), name='other-is-following'),
    path('<int:pk>/followed-by/', GeneralFollowedByListView.as_view(), name='other-is-followed-by'),
]
