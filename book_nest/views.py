from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status
from .utils import recommend_books
from rest_framework.permissions import IsAuthenticated


class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, updating, and deleting books.

    This viewset provides standard CRUD operations for books. It requires that the user be a superuser
    for creating, updating, or deleting books. Users can search for books by title, author name, description, or category.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    search_fields = ["title", "auther__name", "description", "category"]

    def create(self, request, *args, **kwargs):
        """
        Create a new book instance.

        Only superusers are allowed to perform this action. If the request user is not a superuser,
        a PermissionDenied exception will be raised.

        Args:
            request (Request): The HTTP request object containing book data.

        Returns:
            Response: The response object with the created book details.
        """

        if not request.user.is_superuser:
            raise PermissionDenied("You do not have permission to perform this action.")
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Update an existing book instance.

        Only superusers are allowed to perform this action. If the request user is not a superuser,
        a PermissionDenied exception will be raised.

        Args:
            request (Request): The HTTP request object containing updated book data.

        Returns:
            Response: The response object with the updated book details.
        """

        if not request.user.is_superuser:
            raise PermissionDenied("You do not have permission to perform this action.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Delete a book instance.

        Only superusers are allowed to perform this action. If the request user is not a superuser,
        a PermissionDenied exception will be raised.

        Args:
            request (Request): The HTTP request object for deleting the book.

        Returns:
            Response: The response object with status 204 No Content upon successful deletion.
        """

        if not request.user.is_superuser:
            raise PermissionDenied("You do not have permission to perform this action.")
        return super().destroy(request, *args, **kwargs)


class AutherViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, updating, and deleting authors.

    This viewset provides standard CRUD operations for authors. It requires that the user be a superuser
    for creating, updating, or deleting authors. Users can search for authors by name or biography.
    """

    queryset = Auther.objects.all()
    serializer_class = AutherSerializer
    filter_backends = [SearchFilter]
    search_fields = ["name", "biography"]

    def create(self, request, *args, **kwargs):
        """
        Create a new author instance.

        Only superusers are allowed to perform this action. If the request user is not a superuser,
        a PermissionDenied exception will be raised.

        Args:
            request (Request): The HTTP request object containing author data.

        Returns:
            Response: The response object with the created author details.
        """

        if not request.user.is_superuser:
            raise PermissionDenied("You do not have permission to perform this action.")
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Update an existing author instance.

        Only superusers are allowed to perform this action. If the request user is not a superuser,
        a PermissionDenied exception will be raised.

        Args:
            request (Request): The HTTP request object containing updated author data.

        Returns:
            Response: The response object with the updated author details.
        """

        if not request.user.is_superuser:
            raise PermissionDenied("You do not have permission to perform this action.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Delete an author instance.

        Only superusers are allowed to perform this action. If the request user is not a superuser,
        a PermissionDenied exception will be raised.

        Args:
            request (Request): The HTTP request object for deleting the author.

        Returns:
            Response: The response object with status 204 No Content upon successful deletion.
        """

        if not request.user.is_superuser:
            raise PermissionDenied("You do not have permission to perform this action.")
        return super().destroy(request, *args, **kwargs)


class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return the list of favorite books for the current user.
        """
        user = self.request.user
        return Favorite.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        """
        Add a book to the current user's favorites and return recommendations.
        """
        book_id = request.data.get("book")
        if not Book.objects.filter(id=book_id).exists():
            return Response(
                {"error": "Book not found."}, status=status.HTTP_400_BAD_REQUEST
            )

        data = {"user": request.user.id, "book": book_id}
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            self.perform_create(serializer)
            user_favorites = (
                self.get_queryset()
            )  # Ensure it gets favorites for the logged-in user
            recommended_books = recommend_books(user_favorites)
            return Response(
                {
                    "message": "Book added to favorites successfully",
                    "recommendations": [book.title for book in recommended_books],
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """
        Remove a book from the current user's favorites.
        """
        book_id = self.kwargs.get("pk")
        try:
            favorite = Favorite.objects.get(user=request.user, book_id=book_id)
            self.perform_destroy(favorite)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Favorite.DoesNotExist:
            return Response(
                {"error": "Favorite not found."}, status=status.HTTP_404_NOT_FOUND
            )
