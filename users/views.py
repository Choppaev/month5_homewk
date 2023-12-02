import random

from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from django.contrib.auth.models import User
from rest_framework.views import APIView

from .models import UserConfirmation
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserConfirmationSerializer


class RegistrationAPIView(APIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(**serializer.validated_data, is_active=False)
        confirmation = UserConfirmation.objects.create(user=user, code=random.randint(100000, 999999))
        return Response({'status': 'User registered', 'code': confirmation.code, 'data': serializer.data},
                        status=status.HTTP_201_CREATED)


class ConfirmUserAPIView(APIView):
    serializer_class = UserConfirmationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data.get('code')
        confirmation = get_object_or_404(UserConfirmation, code=code)
        user = confirmation.user
        user.is_active = True
        user.save()
        confirmation.delete()
        return Response({'status': 'User activated'}, status=status.HTTP_200_OK)


class AuthorizationAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        login(request, user)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({'message': 'User logged out'}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({'message': 'User is already logged out'}, status=status.HTTP_200_OK)