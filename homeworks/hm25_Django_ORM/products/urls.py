from django.urls import path
from .views import add_product, product_details, products, show_categories, add_category, category_page

urlpatterns = [
    path("/add", add_product, name="add_product"),
    path("/<int:id>", product_details, name="product_details"),
    path("/", products, name="products"),
    path("/categories", show_categories, name="show_categories"),
    path("/category/add", add_category, name="add_category"),
    path("/category/<title>", category_page, name="category_page"),
]
