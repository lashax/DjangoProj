from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions

from listings.models import Clothes, Brand
from listings.serializers import (UserSerializer, ClothesSerializer,
                                  RegisterSerializer)
from .permissions import IsOwnerOrReadOnly


class ClothesList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer

    def perform_create(self, serializer):
        serializer.save(designer=self.request.user)


class ClothesDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer


class RegisterView(generics.CreateAPIView):
    permission_classes = (~IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListBrands(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        brands = [brand.name for brand in Brand.objects.all()]
        return Response(brands)
