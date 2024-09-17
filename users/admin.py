from django.contrib import admin
from .models import *


class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin View for user in django admin panel

    """

    list_display = ["user"]


admin.site.register(UserProfile, UserProfileAdmin)
