from decimal import Decimal
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.db.models import Q
from django.views.decorators.http import require_POST
import stripe

from .models import Product
from .cart import Cart

stripe.api_key = settings.STRIPE_SECRET_KEY


def index(request, view_cart=False):
    """
    Landing page that can display featured products or the cart details.
    """
    cart = Cart(request)
    context = {"cart": cart}

    if view_cart:
        # User wants to see the cart on the homepage
        context["show_cart_view"] = True
    else:
        # Default behavior: show the product listing
        featured_product_names = ["Geaux2", "Sunshine", "Creole Curry"]
        products = Product.objects.filter(
            Q(name__in=featured_product_names) & Q(available=True) & Q(stock__gt=1)
        )
        context["products"] = products
        context["show_cart_view"] = False

    return render(request, "landing/home.html", context)


def cart_add(request, product_id):
    """
    Adds a product to the cart and redirects to the view_cart page.
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    # Redirect to the home page with the cart view active
    return redirect("landing:view_cart_on_home")


def cart_remove(request, product_id):
    """
    Removes a product from the cart and redirects to the cart detail page.
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("landing:cart_detail")


def cart_detail(request):
    """
    Displays the cart details.
    """
    cart = Cart(request)
    return render(request, "landing/cart/detail.html", {"cart": cart})


def checkout(request):
    """
    Handles the Stripe Checkout session creation.
    """
    cart = Cart(request)
    if not cart:
        return redirect("landing:home")

    items = []
    for item in cart:
        items.append(
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": item["product"].name,
                    },
                    "unit_amount": int(item["price"] * 100),
                },
                "quantity": item["quantity"],
            }
        )

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=items,
        mode="payment",
        success_url=request.build_absolute_uri(reverse("landing:payment_success")),
        cancel_url=request.build_absolute_uri(reverse("landing:payment_cancelled")),
    )

    return redirect(checkout_session.url, code=303)


def payment_success(request):
    """
    Handles successful payment.
    """
    cart = Cart(request)
    cart.clear()
    return render(request, "landing/payment/success.html")


def payment_cancelled(request):
    """
    Handles cancelled payment.
    """
    return render(request, "landing/payment/cancelled.html")
