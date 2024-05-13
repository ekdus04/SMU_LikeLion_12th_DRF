from django.urls import path

from posts import views

urlpatterns = [
    path('', views.post_list_api_view, name='post-list'),
    path('<int:posts_id>/', views.post_retrieve_api_view, name='post-retrieve'),
    path('postcomment/<int:comments_id>', views.post_comment_api_view, name='post-comment'),
    path('likes/<int:likes_id>/', views.post_like_api_view, name='post-like'),
    path('comments/<int:comments_id>/', views.new_comment_api_view, name='post-newcomment'),
]
