from . models import Cart,CartItem
from . views import _cart_id
def Counter(request):
    item_cound=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=Cart.objects.filter(cart_id=_cart_id(request))
            cart_items=CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                item_cound += cart_item.quantity
        except Cart.DoesNotExist:
            item_cound=0
    return dict(item_cound=item_cound)


