from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from listings import views as listing_views

router = DefaultRouter()
router.register(r'products', listing_views.ProductViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('listings.urls')),
    path('', include('users.urls')),
]
