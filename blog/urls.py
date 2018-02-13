from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.FeedView.as_view(), name='feed'),
    path('<int:pk>/', views.PostView.as_view(), name='post'),
]
