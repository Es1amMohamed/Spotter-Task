from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

app_name = "book_nest"


router = DefaultRouter()  # Create a router and register our viewsets with it.
router.register("books", BookViewSet)
router.register("authers", AutherViewSet)
router.register("favorites", FavoriteBookViewSet, basename="favorite")

urlpatterns = [
    path(
        "", include(router.urls)
    ),  # The API URLs are now determined automatically by the router.
]
