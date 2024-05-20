from django.urls import path
from rest_framework.routers import DefaultRouter
from posts import views

# urlpatterns = [
#     path('', views.post_list_api_view, name='post-list'),
#     path('<int:post_id>/', views.post_retrieve_api_view, name='post-retrieve'),
#     path('comments/<int:post_id>/', views.comment_list_api_view, name='comment-list'),
#     path('comment/<int:comment_id>/', views.comment_retrieve_api_view, name='comment-retrieve'),
#     path('likes/<int:post_id>/', views.like_api_view, name='like'),
# ]

router = DefaultRouter()
router.register(r'users', views.PostViewSet)

urlpatterns += router.urls

