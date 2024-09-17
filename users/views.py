from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import *
from django.contrib.auth.hashers import make_password
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken


class SignUpAPIView(APIView):
    """
    View to handle user registration.

    This view allows users to register by providing their first name, last name,
    email, and password. If the registration is successful, it creates a new user
    and returns a success message.

    Methods
    -------
    post(request):
        Registers a new user and returns a JWT token if successful.
    """

    def post(self, request):
        data = request.data
        user_serializer = SignupSerializer(data=data)

        if user_serializer.is_valid():
            if not User.objects.filter(email=data["email"]).exists():
                user = User.objects.create(
                    first_name=data["first_name"],
                    last_name=data["last_name"],
                    email=data["email"],
                    username=data["email"],
                    password=make_password(data["password"]),
                )
                login(request, user)
                refresh = RefreshToken.for_user(user)
                return Response(
                    {"message": "Your account created successfully"},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {"message": "Email already exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    """
    View to handle user login.

    This view allows users to log in by providing their username and password.
    If the credentials are correct, it returns a success message.

    Methods
    -------
    post(request):
        Authenticates the user and returns a welcome message if credentials are valid.
    """

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            return Response(
                {"message": f"Welcome, {username}"}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
            )
