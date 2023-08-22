from django.urls import path
from ..apis import customer


urlpatterns = [
    path("", customer.CustomerLoginAPI.as_view(), name="customer_login"),
    path("logout", customer.CustomerLogOutAPI.as_view(), name="customer_logout"),
    path("register", customer.CustomerRegisterAPI.as_view(), name="customer_register"),
    path("product/list", customer.CustomerProductListAPI.as_view(), name="customer_productlist"),
    path("product/create", customer.CreateProductAPI.as_view(), name="product_create"),
    path('product/delete/<int:id>', customer.DeleteProductAPI.as_view(), name="product_delete"),
    path('product/update/<int:id>', customer.UpdateProductAPI.as_view(), name="product_update"),
    path('product/disable', customer.DisableProductAPI.as_view(), name="product_disable"),
]