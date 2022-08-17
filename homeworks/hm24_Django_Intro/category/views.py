from django.shortcuts import render, redirect, get_object_or_404
from main.models import MenuItem
from .models import Category


def category(request):
    menu_items = MenuItem.objects.all()
    # if request.method == 'GET':
    #     category_id = int(request.GET.get('category_id', default=1))
    #     current_category = Category.objects.get(pk=category_id)
    #
    #     children = current_category.get_children()
    #     ancestors = current_category.get_ancestors()
    #     products = current_category.products.all()
    #
    #     context = {
    #         'categories': children,
    #         'current_category': current_category,
    #         'ancestors': ancestors,
    #         'products': products,
    #     }
    #
    # return render(request, 'category/category.html', context, {"menu_items": menu_items})
    return render(request, 'category/category.html', {
        "menu_items": menu_items
    })
