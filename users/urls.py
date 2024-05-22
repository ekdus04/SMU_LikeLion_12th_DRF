from django.urls import path

from users import views

app_name='users'

urlpatterns = [
    # path('', views.user_list_api_view, name='user-list'),
    # path('<int:user_id>/', views.user_retrieve_api_view, name='user-retrieve'),  
    path('', views.UserCreateView.as_view(), name='users-create'),
    path('<int:user_id>/', views.UserAPIView.as_view(), name='users'),
    path('login/', views.jwt_api_view, name='user-login'),
    path('changepwd/<int:user_id>/', views.patch_password_api_view, name='user-password'),
]
