"""clothes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from listings import views as listing_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clothes/', listing_views.ClothesList.as_view()),
    path('clothes/<int:pk>', listing_views.ClothesDetail.as_view()),
    path('users/', listing_views.UserList.as_view()),
    path('users/<int:pk>/', listing_views.UserDetail.as_view()),
    path('api-auth/register/', listing_views.RegisterView.as_view(),
         name='auth_register'),
    path('brands/', listing_views.ListBrands.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
