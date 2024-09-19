from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
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


class FavoriteBookViewSet(viewsets.ModelViewSet):
    """
    ViewSet to manage user's favorite books.

    Provides functionality for:
    - Adding a book to the user's favorites list.
    - Removing a book from the user's favorites list.
    - Retrieving book recommendations based on the user's favorites list.
    """

    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Overrides the default queryset to return only the favorite books for the authenticated user.
        """

        return Favorite.objects.filter(user=self.request.user)

    @action(detail=False, methods=["post"])
    def add_favorite(self, request):
        """
        POST action to add a book to the user's favorites list.

        Parameters:
            - book_id (int): The ID of the book to be added to the favorites.

        Returns:
            - A success message if the book is added successfully.
            - An error message if the book does not exist.
        """
        book_id = request.data.get("book")
        user = request.user

        # Debugging output to verify book_id
        print(f"book_id received: {book_id}")

        try:
            book = Book.objects.get(id=book_id)
            user_id = User.objects.get(id=user.id)
            # Check if the book is already in the user's favorites
            if Favorite.objects.filter(user=user_id, book=book).exists():
                return Response(
                    {"message": "Book is already in your favorites."}, status=400
                )

            # Add the book to the favorites if it's not already there
            Favorite.objects.create(user=user_id, book=book)
            return Response({"message": "Book added to favorites"})

        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=404)
        except ValueError:
            return Response({"error": "Invalid book ID format"}, status=400)

    @action(detail=True, methods=["delete"])
    def remove_favorite(self, request, pk=None):
        """
        DELETE action to remove a book from the user's favorites list.

        URL Parameter:
            - pk (int): The ID of the book to be removed from the favorites.

        Returns:
            - A success message if the book is removed successfully.
            - An error message if the favorite book does not exist.
        """

        user = request.user
        try:
            favorite = Favorite.objects.get(user=user, book_id=pk)
            favorite.delete()
            return Response({"message": "Book removed from favorites"})
        except Favorite.DoesNotExist:
            return Response({"error": "Favorite book not found"}, status=404)

    @action(detail=False, methods=["get"])
    def recommendations(self, request):
        """
        GET action to retrieve book recommendations based on the user's favorite books.

        Recommendations are based on the categories and authors of the books in the user's favorites list.

        Returns:
            - A list of up to 5 recommended book titles.
            - An error message if no favorite books are found.
        """

        user = request.user
        favorites = Favorite.objects.filter(user=user).values_list(
            "book__id", "book__category", "book__auther"
        )

        if not favorites.exists():
            return Response({"message": "No favorite books found."}, status=404)

        categories = [fav[1] for fav in favorites]
        authors = [fav[2] for fav in favorites]
        favorite_ids = [fav[0] for fav in favorites]
        recommended_books = Book.objects.filter(category__in=categories).exclude(
            id__in=favorite_ids
        )[:5]

        return Response({"recommendations": [book.title for book in recommended_books]})
