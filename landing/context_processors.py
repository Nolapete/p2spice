from .cart import Cart


def cart(request):
    """
    Makes the cart available to all templates.
    """
    return {"cart": Cart(request)}
