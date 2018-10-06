from django.urls import path
from .views import validate_wx_token, obtain_token, GetUserInfoView


urlpatterns = [
    path("validate", validate_wx_token),
    path("obtainToken", obtain_token),
    path("users/<int:userId>/", GetUserInfoView.as_view()),
]
