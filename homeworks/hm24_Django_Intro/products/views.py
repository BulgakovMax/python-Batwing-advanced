from django.shortcuts import render, redirect, get_object_or_404

from main.models import MenuItem
from .models import Product


def add_product(request):
    menu_items = MenuItem.objects.all()
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "products/add.html", {"menu_items": menu_items})
        else:
            product = Product()
            product.title = request.POST.get("title")
            product.description = request.POST.get("description")
            product.user = request.user
            product.save()
            return redirect("/")
    else:
        return redirect("/")


def product_details(request, id):
    menu_items = MenuItem.objects.all()
    product = get_object_or_404(Product, id=id)
    return render(request,  "products/details.html", {"menu_items": menu_items, "product": product})


def products(request):
    menu_items = MenuItem.objects.all()
    products_list = Product.objects.filter(display_on_main_page=True, approved=True).order_by("title").values()
    return render(request, 'products/products.html', {
        "menu_items": menu_items,
        "products_list": products_list
    })
