from django.urls import path
from .views import (
    my_fbv,
    CourseView,
    CourseListView,
    CourseCreateView,
)

app_name = 'courses'
urlpatterns = [
    # path('', my_fbv, name='courses-list'),
    path('', CourseListView.as_view(), name='courses-list'),
    path('create/', CourseCreateView.as_view(), name='courses-create'),
    path('<int:id>/', CourseView.as_view(), name='course-detail'),
    # path('<int:id>/update/', product_update_view, name='product-update'),
    # path('<int:id>/delete/', product_delete_view, name='product-delete'),
]
