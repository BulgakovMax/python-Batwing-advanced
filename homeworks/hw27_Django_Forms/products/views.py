from django.shortcuts import render, redirect, get_object_or_404
from main.models import MenuItem
from .models import Product, Category
from .forms import ProductForm
from django.http import Http404


def add_product(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            categories = Category.objects.order_by("-id")
            form = ProductForm(initial={
                "user": request.user,
                "title": "lol"
            })
            return render(request, "products/add.html", {"form": form, "categories": categories})
        else:
            form = ProductForm(request.POST)
            if form.is_valid():
                product = form.save(user=request.user)
                if request.POST.getlist("categories", False):
                    print(request.POST.getlist("categories"))
                    for category_id in request.POST.getlist("categories"):
                        category_id = int(category_id)
                        category = Category.objects.get(id=category_id)
                        category.products.add(product)
                return redirect("/")
            else:
                return render(request, "products/add.html", {"form": form})
    else:
        return redirect("/")


def edit_product(request, id):
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
                return render(request, "products/edit_product.html", {"product": product})
        else:
            return HttpResponseForbidden()
    else:
        return redirect("/")


def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    if product.id in request.session.get("products", []):
        return render(request, "products/details.html", {"product": product, "button_status": "btn-secondary disabled"})
    return render(request, "products/details.html", {"product": product, "button_status": "btn-success active"})


def products(request):
    products_list = Product.objects.filter(display_on_main_page=True, approved=True).order_by("title").values()
    return render(request, 'products/products.html', {"products_list": products_list})


def add_category(request):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == "POST":
            if request.POST.get("title"):
                category = Category()
                category.user = request.user
                category.title = request.POST.get("title")
                category.slug = request.POST.get("slug")
                if request.POST.get("parent_category", False):
                    category.parent_id = int(request.POST.get("parent_category"))
                category.save()
                return redirect("/")
        else:
            categories = Category.objects.order_by("-id")
            return render(request, "products/category/add.html", {"categories": categories})
    else:
        return redirect("/")


def category_page(request, slug):
    try:
        category = Category.objects.get(slug=slug)
    except Category.DoesNotExist:
        raise Http404()
    return render(request, "products/category_products.html", {"products": category.products.all()})


def update_product(request, id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=id)
        if product.user_id == request.user.id:
            if request.method == "GET":
                categories = Category.objects.order_by("-id")
                return render(request, "products/update.html", {"product": product, "categories": categories})
            else:
                product.title = request.POST.get("title", "")
                product.description = request.POST.get("description", "")
                product.price = request.POST.get("price", "")
                product.save()
                if request.POST.getlist("categories", False):
                    print(request.POST.getlist("categories"))
                    for category_id in request.POST.getlist("categories"):
                        category_id = int(category_id)
                        category = Category.objects.get(id=category_id)
                        category.products.add(product)
                return redirect("/")
    return redirect("/")


def categories(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    return render(request,  'products/categories.html', context)


def update_category(request, id):
    if request.user.is_authenticated:
        category = Category.objects.get(id=id)
        if category.user_id == request.user.id:
            if request.method == "GET":
                return render(request, "products/category/update.html", {"category": category})
            else:
                category.title = request.POST.get("title", "")
                category.slug = request.POST.get("slug", "")
                category.save()
                return redirect("/")
    return redirect("/")

