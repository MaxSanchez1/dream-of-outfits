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
    FollowAProfileToggle,
    OtherOutfitListView,
    OtherArticleListView,
    OtherCollectionListView,
    EditPersonalProfile,
)


app_name = 'userprofiles'
urlpatterns = [
    path('', AllProfilesView.as_view(), name='all-profiles'),  # just for debugging, only for staff
    path('my-profile/', PersonalProfileView.as_view(), name='my-profile'),
    path('my-profile/edit/', EditPersonalProfile.as_view(), name='edit-my-profile'),
    path('my-profile/following/', PersonalFollowingListView.as_view(), name='i-am-following'),
    path('my-profile/followed-by/', PersonalFollowedByListView.as_view(), name='i-am-followed-by'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/their-outfits/', OtherOutfitListView.as_view(), name='profiles-outfits'),
    path('profile/<int:pk>/their-articles/', OtherArticleListView.as_view(), name='profiles-articles'),
    path('profile/<int:pk>/their-collections/', OtherCollectionListView.as_view(), name='profiles-collections'),
    path('profile/<int:pk>/follow/', FollowAProfileToggle.as_view(), name='toggle-follow'),
    path('profile/<int:pk>/following/', GeneralFollowingListView.as_view(), name='other-is-following'),
    path('profile/<int:pk>/followed-by/', GeneralFollowedByListView.as_view(), name='other-is-followed-by'),
]
