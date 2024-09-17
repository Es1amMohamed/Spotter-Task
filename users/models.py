from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    A model that extends the User model to include additional profile information.

    Each user has a one-to-one relationship with a UserProfile. The UserProfile model
    is automatically created for each user upon their creation, except for superusers.
    """

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} Profile"

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create a UserProfile instance when a new User is created, unless the user is a superuser.

    This signal receiver is triggered after a User instance is saved. If the user is newly created
    and is not a superuser, a corresponding UserProfile instance is created for them.

    Args:
        sender (Model): The model class that sent the signal (User in this case).
        instance (User): The instance of the model that is being saved.
        created (bool): Whether a new record was created.
        **kwargs: Additional keyword arguments passed by the signal.
    """

    if created and not instance.is_superuser:
        UserProfile.objects.create(user=instance)
