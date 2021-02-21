from django.urls import path, include
from rest_framework import urlpatterns
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'user'

router = DefaultRouter()

router.register('profile', views.ProfileViewSet)
router.register('post', views.PostViewSet)
router.register('commentt', views.CommentViewSet)

urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('myplofile/', views.MyPlofileListView.as_view(), name='myplofile'),
    path('', include(router.urls))
]