from django.contrib.auth.models import User
from django.db import models

from items.models import Item


class CartItem(models.Model):
    item = models.ForeignKey(Item, related_name="cart_items", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="cart_items", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.item} | Quantity: {self.quantity} | User: @{self.cart.user}"
