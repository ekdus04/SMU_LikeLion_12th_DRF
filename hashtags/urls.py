from django.urls import path

from hashtags import views

urlpatterns = [
    path('', views.hashtag_list_api_view, name='hashtag-list'),
    path('<int:hashtags_id>/', views.hashtag_retrieve_api_view, name='hashtag-retrieve'),
]