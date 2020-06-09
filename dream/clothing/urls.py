from django.urls import path

# import views here once they're added
from .views import (
    OutfitListView,
    OutfitDetailView,
    FavoritedOutfitListView,
)


app_name = 'clothing'
urlpatterns = [
    path('', OutfitListView.as_view(), name='outfit-list'),
    path('<int:pk>/', OutfitDetailView.as_view(), name='outfit-detail'),
    path('favorite-outfits/', FavoritedOutfitListView.as_view(), name='favorite-outfit-list'),
]
