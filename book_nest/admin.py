from django.contrib import admin
from .models import *


class BookAdmin(admin.ModelAdmin):
    """
    Admin View for user in django admin panel

    """

    list_display = ["title", "auther", "category"]
    list_filter = ["title", "auther"]
    search_fields = ["title", "auther__name"]


class AutherAdmin(admin.ModelAdmin):
    """
    Admin View for user in django admin panel

    """

    list_display = ["name", "nationality"]
    list_filter = ["name", "nationality"]
    search_fields = [
        "name",
    ]


admin.site.register(Book, BookAdmin)
admin.site.register(Auther, AutherAdmin)
admin.site.register(Favorite)
