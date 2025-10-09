from django.urls import path, re_path
from . import views

app_name = "landing"

urlpatterns = [
    path("", views.index, name="home"),
    # URL for viewing the cart on the homepage
    path("view_cart/", views.index, {"view_cart": True}, name="view_cart_on_home"),
    # Existing cart and payment URLs
    path("add-to-cart/<int:product_id>/", views.cart_add, name="cart_add"),
    path("cart/", views.cart_detail, name="cart_detail"),
    path("remove-from-cart/<int:product_id>/", views.cart_remove, name="cart_remove"),
    path("checkout/", views.checkout, name="checkout"),
    path("payment/success/", views.payment_success, name="payment_success"),
    path("payment/cancelled/", views.payment_cancelled, name="payment_cancelled"),
]
