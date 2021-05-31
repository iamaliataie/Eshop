from django.urls import path

from novinfajr_account.views import login_page, signup_page

urlpatterns = [
    path('login', login_page, name='login'),
    path('register', signup_page, name='signup'),
]