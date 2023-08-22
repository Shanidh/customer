from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Status(models.TextChoices):
    ACTIVATE = "ACTIVATE", _("Activate")
    DISABLE = "DISABLE", _("Disable")


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.BigIntegerField()
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(
        help_text=_("Product Status"),
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVATE,
        null=True,
        )
    
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="product_user",
        null=True,
    )

    @property
    def is_inactive(self):
        two_months_ago = timezone.now() - timezone.timedelta(days=60)
        return self.created_date <= two_months_ago

    def update_status(self):
        if self.is_inactive:
            self.status = Status.DISABLE
            self.save()