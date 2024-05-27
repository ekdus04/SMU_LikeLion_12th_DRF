from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet
from posts import views


router = DefaultRouter()
router.register(r'', PostViewSet)

urlpatterns = [
    # path('', views.post_list_api_view, name='post-list'),
    # path('<int:post_id>/', views.post_retrieve_api_view, name='post-retrieve'),
    path('', include(router.urls)),
    path('comments/<int:post_id>/', views.comment_list_api_view, name='comment-list'),
    path('comment/<int:comment_id>/', views.comment_retrieve_api_view, name='comment-retrieve'),
    # path('likes/<int:post_id>/', views.LikeView.as_view(), name='like'),
]