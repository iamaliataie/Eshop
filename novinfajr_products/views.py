from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from novinfajr_order.forms import UserNewOrder
from novinfajr_products.models import Product
from novinfajr_products_category.models import ProductCategory


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/product_list.html'
    paginate_by = 9

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        sidebar = Product.objects.all()
        context['page_title'] = 'محصولات'
        context['products'] = sidebar
        return context


def product_detail(request, *args, **kwargs):
    product_id = kwargs['productId']
    user_order_form = UserNewOrder(request.POST or None, initial={'product_id': product_id})

    product = Product.objects.get_porduct_by_id(product_id)
    products = Product.objects.all()

    context = {
        'page_title': product.title,
        'product': product,
        'products': products,
        'order_form': user_order_form,
    }
    return render(request, 'products/product_detail.html', context)


class ProductListViewByCategory(ListView):
    template_name = 'products/product_list.html'
    paginate_by = 9

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        return Product.objects.get_product_by_category(category_name)

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(ProductListViewByCategory, self).get_context_data(*args, **kwargs)
        category_name = self.kwargs['category_name']
        category_title = ProductCategory.objects.get(URL=category_name)
        context['page_title'] = category_title
        return context


def sidebar(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()

    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'products/shared/sidebar.html', context)