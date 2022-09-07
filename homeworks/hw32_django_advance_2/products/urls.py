from django.urls import path
from .views import \
    add_category, category_page, categories, update_category,\
    add_product, update_product, edit_product, products, product_details

urlpatterns = [
    path("/", products, name="products"),
    path("/add", add_product, name="add_product"),
    path("/update/<int:id>", update_product, name="update_product"),
    path("/edit_product/<int:id>", edit_product, name="edit_product"),
    path("/category/add", add_category, name="add_category"),
    path("/category/update/<int:id>", update_category, name="update_category"),
    path("/categories", categories, name="categories"),
    path("/<int:id>", product_details, name="product_details"),
    path("/category/<str:slug>", category_page, name="category_page")
]