from django.contrib.auth import login, logout
from django.shortcuts import redirect, render

from novinfajr_client_comment.models import ClientComment
from novinfajr_order.models import Order
from novinfajr_products.models import Product
from novinfajr_products_category.models import ProductCategory


def home_page(request):
    products = Product.objects.all()
    comments = ClientComment.objects.all()
    categories = ProductCategory.objects.all()
    context = {
        'page_title': 'خانه',
        'products': products,
        'comments': comments,
        'categories': categories
    }
    return render(request, 'homepage.html', context)


def header(request):
    context = {
        'ordercount': None
    }
    order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if order is None:
        context['ordercount'] = 0
        return render(request, 'shared/Header.html', context)
    order_detail = order.orderdetail_set.all().count()

    context['ordercount'] = order_detail
    return render(request, 'shared/Header.html', context)


def log_out(request):
    logout(request)
    return redirect('/')