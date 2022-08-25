from django.shortcuts import render, redirect, get_object_or_404

from main.models import MenuItem
from .models import Product, Category


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


def edit_product(request, id):
    menu_items = MenuItem.objects.all()
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=id)
        if product.user == request.user:
            if request.method == "POST":
                product.title = request.POST.get("title")
                product.description = request.POST.get("description")
                product.user = request.user
                product.save()
                return redirect("/")
            else:
                return render(request, "products/edit_product.html", {"menu_items": menu_items, "product": product})
        else:
            return HttpResponseForbidden()
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


def show_categories(request):
    menu_items = MenuItem.objects.all()
    categories = Category.objects.all()

    context = {
        'categories': categories,
        "menu_items": menu_items,
    }
    return render(request,  'products/categories.html', context)


def add_category(request):
    menu_items = MenuItem.objects.all()
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == "POST":
            if request.POST.get("title"):
                category = Category()
                category.user = request.user
                category.title = request.POST.get("title")
                category.save()
                return redirect("/")
        else:
            categories = Category.objects.order_by("-id")
            return render(request, "products/category/add.html", {"categories": categories, "menu_items": menu_items})


def category_page(request, title):
    menu_items = MenuItem.objects.all()
    try:
        category = get_object_or_404(Category, title=title)
        product_list = category.products.all()
    except Category.DoesNotExist:
        raise Http404()
    return render(request, "products/category_products.html", {"menu_items": menu_items, "category": category,
                                                               "product_list": product_list})
