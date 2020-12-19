from django.urls import path
from .views import (
    IndexView,
    CreatePostView,
)


app_name = 'main'

urlpatterns=[
    path('', IndexView.as_view(), name='index'),
    path('create/', CreatePostView.as_view(), name='create')
]