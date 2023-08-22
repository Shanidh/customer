from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

# Create your models here.
class CustomUser(AbstractUser):
    """Model definition for User."""

    error_messages = {"slug": {"unique": "Username Already Exists."}}

    first_name = None
    last_name = None
    groups = None
    user_permissions = None
    date_joined = None 

    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        """Unicode representation of User."""
        return self.username

    def save(self, *args, **kwargs):
        """Save method for User."""
        self.slug = slugify(self.username)
        return super().save(*args, **kwargs)