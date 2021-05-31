from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری خود را وارد کنید', 'class': 'form-control'}),
        label='نام کاربری'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز خود را وارد کنید', 'class': 'form-control'}),
        label='رمز عبور'
    )


class UserRegisterForm(forms.Form):
    firstname = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام', 'class': 'form-control'}),
        label='نام'
    )

    lastname = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی', 'class': 'form-control'}),
        label='نام خانوادگی'
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری خود را وارد کنید', 'class': 'form-control'}),
        label='نام کاربری'
    )

    email = forms.CharField(
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل خود را وارد کنید', 'class': 'form-control'}),
        label='ایمیل'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز خود را وارد کنید', 'class': 'form-control'}),
        label='رمز عبور'
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'تایید رمز عبور', 'class': 'form-control'}),
        label='تایید رمز عبور'
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if confirm_password != password:
            raise forms.ValidationError('رمزهای وارد شده مغایرت دارند')

        return password