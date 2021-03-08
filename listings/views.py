from rest_framework import generics, viewsets
from rest_framework import permissions

from listings.models import Product, Brand
from listings.serializers import ProductSerializer, BrandSerializer
from .paginations import PaginationPerTen
from .permissions import IsOwnerOrReadOnly


class BrandList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    pagination_class = PaginationPerTen


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(designer=self.request.user)
