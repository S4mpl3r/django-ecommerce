from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Item


# Create your views here.
def index(request):
    items = get_list_or_404(Item, is_sold=False)[:8]
    for item in items:
        if item.is_on_sale:
            item.discount = item.discounted_price()
    return render(
        request,
        "items/index.html",
        {
            "items": items,
        },
    )


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if item.is_on_sale:
        item.discount = item.discounted_price()
    return render(
        request,
        "items/detail.html",
        {
            "item": item,
        },
    )
