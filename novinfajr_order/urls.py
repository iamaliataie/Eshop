from django.urls import path

from novinfajr_order.views import add_user_order, user_open_order, remove_order, check_out

urlpatterns = [
    path('add-user-order', add_user_order),
    path('open-order', user_open_order, name='cart'),
    path('remove-order/<orderdetailId>', remove_order),
    path('checkout/<orderId>', check_out),
]