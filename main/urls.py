from django.urls import path
from .views import (
    IndexView,
    UserPostsView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView
)


app_name = 'main'

urlpatterns=[
    path('', IndexView.as_view(), name='index'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
    path('user/<str:username>/', UserPostsView.as_view(), name='user-post'),
]