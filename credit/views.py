from django.shortcuts import render
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets, generics, mixins
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied

from . import models
from . import serializers

# Create your views here.


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.ower == request.user


class CreditPersoViewset(viewsets.ModelViewSet):

    serializer_class = serializers.CreditSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return models.Credit.objects.filter(ower=user)
        raise PermissionDenied()

    def perform_create(self, serializer):
        serializer.save(ower=self.request.user)