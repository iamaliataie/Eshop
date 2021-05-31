from django.urls import path

from .views import product_detail, ProductListView, ProductListViewByCategory, sidebar

urlpatterns = [
    path('products', ProductListView.as_view(), name='products'),
    path('product/<productId>/<title>', product_detail),
    path('products/category/<category_name>', ProductListViewByCategory.as_view()),
    path('sidebar', sidebar, name='sidebar')
]
