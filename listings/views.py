from .permissions import IsOwnerOrReadOnly, IsNotAuthenticated
from listings.models import Clothes
from listings.serializers import ClothesSerializer, RegisterSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions

from listings.serializers import UserSerializer


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
    permission_classes = (IsNotAuthenticated, )
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
