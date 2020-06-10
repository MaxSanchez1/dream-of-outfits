from django.urls import path

# import views here once they're added
from .views import (
    OutfitListView,
    OutfitDetailView,
    FavoritedOutfitListView,
    ArticleListView,
    ArticleDetailView,
    FavoritedArticleListView,
)


app_name = 'clothing'
urlpatterns = [
    path('', OutfitListView.as_view(), name='outfit-list'),
    path('<int:pk>/', OutfitDetailView.as_view(), name='outfit-detail'),
    path('favorite-outfits/', FavoritedOutfitListView.as_view(), name='favorite-outfit-list'),
    path('closet/', ArticleListView.as_view(), name='clothing-list'),
    path('closet/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('favorite-articles/', FavoritedArticleListView.as_view(), name='favorite-article-list'),
]
