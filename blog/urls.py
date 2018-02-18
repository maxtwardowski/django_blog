from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.FeedView.as_view(), name='feed'),
    path('<int:pk>/', views.PostView.as_view(), name='post'),
    path('<int:pk>/comment/', views.AddComment, name='comment'),
    path('newpost/', views.AddPostView, name='newpost'),
    path('newpost/addingpost/', views.AddPost, name='post'),
    ]
