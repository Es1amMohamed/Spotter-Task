from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password")
        extra_kwargs = {
            "first_name": {
                "required": True,
                "allow_blank": False,
                "help_text": "The user's first name. This field is required and cannot be blank.",
            },
            "last_name": {
                "required": True,
                "allow_blank": False,
                "help_text": "The user's last name. This field is required and cannot be blank.",
            },
            "email": {
                "required": True,
                "allow_blank": False,
                "help_text": "The user's email address. This field is required and cannot be blank.",
            },
            "password": {
                "required": True,
                "allow_blank": False,
                "min_length": 8,
                "help_text": "The user's password. This field is required, cannot be blank, and must be at least 8 characters long.",
            },
        }
