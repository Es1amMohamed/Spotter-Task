from django.urls import path
from .views import *

app_name = "users"

urlpatterns = [
    path("register/", SignUpAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
]
