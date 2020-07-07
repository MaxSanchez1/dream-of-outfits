from django.urls import path

# import views here once they're added
from .views import (
    OutfitListView,
    OutfitDetailView,
    FavoritedOutfitListView,
    ArticleListView,
    ArticleDetailView,
    FavoritedArticleListView,
    CreateOutfitView,
    CreateArticleView,
    ArticleFavoriteToggle,
    OutfitFavoriteToggle,
    CollectionListView,
    CollectionDetailView,
    CreateCollectionView,
    CollectionUpdateView,
    ArticleDeleteView,
    OutfitDeleteView,
    CollectionDeleteView,
)


app_name = 'clothing'
urlpatterns = [
    path('', OutfitListView.as_view(), name='outfit-list'),
    path('<int:pk>/', OutfitDetailView.as_view(), name='outfit-detail'),
    path('<int:pk>/favorite/', OutfitFavoriteToggle.as_view(), name='outfit-favorite-toggle'),
    path('<int:pk>/delete/', OutfitDeleteView.as_view(), name='outfit-delete'),
    path('favorite-outfits/', FavoritedOutfitListView.as_view(), name='favorite-outfit-list'),
    path('closet/', ArticleListView.as_view(), name='clothing-list'),
    path('closet/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('closet/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    path('closet/<int:pk>/favorite/', ArticleFavoriteToggle.as_view(), name='article-favorite-toggle'),
    path('favorite-articles/', FavoritedArticleListView.as_view(), name='favorite-article-list'),
    path('create-outfit/', CreateOutfitView.as_view(), name='create-new-outfit'),
    path('closet/create-article/', CreateArticleView.as_view(), name='create-new-article'),
    path('collections/', CollectionListView.as_view(), name='collection-list'),
    path('collections/<int:pk>/', CollectionDetailView.as_view(), name='collection-detail'),
    path('collections/<int:pk>/delete/', CollectionDeleteView.as_view(), name='collection-delete'),
    path('collections/create-collection/', CreateCollectionView.as_view(), name='create-new-collection'),
    path('collections/<int:pk>/edit', CollectionUpdateView.as_view(), name='edit-collection'),

]
