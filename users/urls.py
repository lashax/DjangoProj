from django.urls import path, include

from users import views as user_views

urlpatterns = [
    path('users/', user_views.UserList.as_view(), name='users-list'),
    path('users/<int:pk>/', user_views.UserDetail.as_view(),
         name='users-detail'),
    path('api-auth/register/', user_views.RegisterView.as_view(),
         name='users_register'),
    path('api-auth/', include('rest_framework.urls')),
]
