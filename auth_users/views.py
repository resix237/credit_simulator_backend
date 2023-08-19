from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from . import serializers
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer


class createUserGestion(APIView):
    permission_classes = (AllowAny,)

    def post(self, resquest):
        userGestion = resquest.data
        serializer = serializers.UserGestionSerializer(data=userGestion)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
