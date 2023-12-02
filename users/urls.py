from django.urls import path
from users.views import (
    RegistrationAPIView,
    ConfirmUserAPIView,
    AuthorizationAPIView,
    LogoutAPIView
)



urlpatterns = [
    path('users/registration/', RegistrationAPIView.as_view()),
    path('users/confirm/', ConfirmUserAPIView.as_view()),
    path('users/authorization/', AuthorizationAPIView.as_view()),
    path('users/logout/', LogoutAPIView.as_view())
]