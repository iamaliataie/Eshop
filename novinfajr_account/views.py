from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login

# Create your views here.
from novinfajr_account.forms import UserLoginForm, UserRegisterForm

User = get_user_model()


def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    login_form = UserLoginForm(request.POST or None)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            login_form.add_error('password', 'کاربری با مشخصات وارد شده یافت نشد')
            login_form.username = user_name
            login_form.password = password

    context = {
        'page_title': 'ورود',
        'login_form': login_form
    }
    return render(request, 'account/login.html', context)


def signup_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    register_form = UserRegisterForm(request.POST or None)
    context = {
        'page_title': 'ثبت نام',
        'register_form': register_form
    }

    if register_form.is_valid():
        first_name = register_form.cleaned_data.get('firstname')
        last_name = register_form.cleaned_data.get('lastname')
        user_name = register_form.cleaned_data.get('username')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')

        user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                        username=user_name, email=email, password=password)
        if user:
            return redirect('/login')

    return render(request, 'account/signup.html', context)