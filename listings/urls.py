from django.urls import path, include
from rest_framework.routers import DefaultRouter

from listings import views as listing_views


router = DefaultRouter()
router.register(r'products', listing_views.ProductViewSet)

urlpatterns = [
    path('brands/', listing_views.BrandList.as_view()),
    path('', include(router.urls))
]
