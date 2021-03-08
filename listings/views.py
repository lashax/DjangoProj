from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
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


# class RegisterView(generics.CreateAPIView):
#     permission_classes = (~IsAuthenticated,)
#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer
#
#
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
