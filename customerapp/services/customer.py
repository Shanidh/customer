from ..models import CustomUser, Product, Status
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

User = get_user_model()


def create_customer(
    username: str,
    password: str,
) -> None:
    user = CustomUser.objects.create_user(username=username, password=password)


def create_product(
    user: User,
    name: str,
    description: str,
    price: str,
) -> None:
    product = Product(
        name=name,
        description=description,
        price=price,
        user=user,
    )
    product.save()             


def disable_status(user: User, id: int) -> str:
    product = Product.objects.get(pk=id)
    if product.user == user:
        if product.status == Status.ACTIVATE:
            product.status = Status.DISABLE
            product.save()
            return _("Product Disabled")
        else:
            product.status = Status.ACTIVATE
            product.save()
            return _("Product Activated")
    else:
        raise ValidationError(_("You cant change status of this product"))        