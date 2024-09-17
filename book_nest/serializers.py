from rest_framework import serializers
from .models import *


class AutherSerializer(serializers.ModelSerializer):
    """
    Serializer for the Auther model.

    Attributes:
        name (str): The name of the author.
        biography (str): A biography of the author.
        birth_date (date): The birth date of the author.
        nationality (str): The nationality of the author.
        website (URLField): The author's website.
        awards (str): Any awards won by the author.
    """

    class Meta:
        model = Auther
        fields = ["name", "biography", "birth_date", "nationality", "website", "awards"]


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.

    Attributes:
        title (str): The title of the book.
        auther_name (str): The name of the author of the book, derived from the auther model.
        description (str): A description of the book.
        category (str): The category of the book.
        published_date (date): The publication date of the book.
        language (str): The language of the book.
        pages (int): The number of pages in the book.
    """

    auther_name = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            "title",
            "auther_name",
            "description",
            "category",
            "published_date",
            "language",
            "pages",
        ]

    def get_auther_name(self, obj):
        """
        Retrieve the name of the author for a given book.

        Args:
            obj (Book): The book instance.

        Returns:
            str: The name of the author.
        """

        return obj.auther.name


class FavoriteSerializer(serializers.ModelSerializer):
    """
    Serializer for the Favorite model.

    Attributes:
        id (int): The ID of the favorite record.
        user (ForeignKey): The user who marked the book as a favorite.
        book (ForeignKey): The book that has been marked as a favorite.
    """

    class Meta:
        model = Favorite
        fields = ["id", "user", "book"]
