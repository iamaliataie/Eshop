from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from novinfajr_order.forms import UserNewOrder
from novinfajr_order.models import Order, OrderDetail
from novinfajr_products.models import Product


@login_required(login_url='/login')
def add_user_order(request):
    user_order_form = UserNewOrder(request.POST or None)

    if user_order_form.is_valid():
        order: Order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id)
        productId = user_order_form.cleaned_data.get('product_id')
        count = user_order_form.cleaned_data.get('count')

        if count <= 0:
            count = 1

        product = Product.objects.get_porduct_by_id(productId)

        order.orderdetail_set.create(product_id=productId, price=product.price, count=count)

    return redirect(product.get_absolute_url())


@login_required(login_url='/login')
def user_open_order(request):
    context = {
        'order': None ,
        'orderdetail': None,
        'page_title': 'سبد خرید'
    }

    order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if order is None:
        return render(request, 'orders/order_detail.html', context)
    order_detail = order.orderdetail_set.all()
    if order_detail.count() == 0:
        return render(request, 'orders/order_detail.html', context)
    order_detail_count = order.orderdetail_set.all().count()
    print(order_detail_count)
    context['order'] = order
    context['orderdetail'] = order_detail

    return render(request, 'orders/order_detail.html', context)


@login_required(login_url='/login')
def remove_order(request, *args, **kwargs):
    order_detail_id = kwargs['orderdetailId']
    order_detail = OrderDetail.objects.get(id=order_detail_id)
    print(order_detail)
    order_detail.delete()
    return redirect('/open-order')


@login_required(login_url='/login')
def check_out(request, *args, **kwargs):
    order_id = kwargs['orderId']
    open_order = Order.objects.get(id=order_id)
    open_order.is_paid = True
    open_order.save()
    return redirect('/open-order')