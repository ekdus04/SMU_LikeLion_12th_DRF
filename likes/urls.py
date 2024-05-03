from django.urls import path

from likes import views

urlpatterns = [
    path('', views.like_list_api_view, name='like-list'),
    path('<int:like_id>/', views.like_retrieve_api_view, name='like-retrieve'),
]