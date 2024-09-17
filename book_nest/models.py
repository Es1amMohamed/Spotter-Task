from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    """
    Represents a book in the library.

    Attributes:
        title (str): The title of the book.
        auther (ForeignKey): A reference to the author of the book.
        description (str): A description of the book.
        category (str): The category of the book, chosen from predefined choices.
        language (str): The language of the book.
        pages (int): The number of pages in the book.
        published_date (date): The publication date of the book.
        created_at (datetime): The timestamp when the book entry was created.

    Meta:
        verbose_name (str): Singular name for the model.
        verbose_name_plural (str): Plural name for the model.
    """

    CATEGORY_CHOICES = [
        ("NON_FIC", "Non-Fiction"),
        ("HOR", "Horror"),
        ("SF", "Science Fiction"),
        ("FAN", "Fantasy"),
        ("BIO", "Biography"),
        ("HIS", "History"),
        ("PHI", "Philosophy"),
        ("TRA", "Travel"),
        ("SELF_HELP", "Self-Help"),
        ("EDU", "Educational"),
        ("FIC", "Fiction"),
    ]

    title = models.CharField(max_length=100, null=False, blank=False, unique=True)
    auther = models.ForeignKey(
        "Auther", related_name="book_auther", on_delete=models.CASCADE
    )
    description = models.TextField(max_length=500)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default="FIC")
    language = models.CharField(max_length=50, blank=True, null=True)
    pages = models.PositiveIntegerField(blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title


class Auther(models.Model):
    """
    Represents an author in the library.

    Attributes:
        name (str): The name of the author.
        biography (str): A biography of the author.
        birth_date (date): The birth date of the author.
        nationality (str): The nationality of the author.
        website (URLField): The author's website.
        awards (str): Any awards won by the author.
        created_at (datetime): The timestamp when the author entry was created.

    Meta:
        verbose_name (str): Singular name for the model.
        verbose_name_plural (str): Plural name for the model.
    """

    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    awards = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Auther"
        verbose_name_plural = "Authers"

    def __str__(self):
        return self.name


class Favorite(models.Model):
    """
    Represents a user's favorite book.

    Attributes:
        user (ForeignKey): A reference to the user who marked the book as a favorite.
        book (ForeignKey): A reference to the favorite book.

    Meta:
        unique_together (tuple): Ensures that a user can only mark a book as favorite once.
        verbose_name (str): Singular name for the model.
        verbose_name_plural (str): Plural name for the model.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="favorites")

    class Meta:
        unique_together = ("user", "book")
        verbose_name = "Favorite"
        verbose_name_plural = "Favorites"

    def __str__(self):
        return self.user.first_name
