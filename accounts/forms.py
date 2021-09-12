from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=200,
                                widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'ایمیل'}))
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'نام'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی'}))
    password_1 = forms.CharField(max_length=200,
                                 widget=forms.PasswordInput(attrs={'placeholder': 'رمزعبور'}))
    password_2 = forms.CharField(max_length=200,
                                 widget=forms.PasswordInput(attrs={'placeholder': 'تکرار رمز عبور'}))

    def clean_user_name(self):
        user = self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('user exists!')
        return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('email exists!')
        return email

    def clean_password_2(self):
        password_1 = self.cleaned_data['password_1']
        password_2 = self.cleaned_data['password_2']
        if password_1 != password_2:
            raise forms.ValidationError('password not match')
        elif len(password_2) < 8:
            raise forms.ValidationError('password is too short')
        elif not any(x.isupper() for x in password_2):
            raise forms.ValidationError('password dose not have any capital character')


class UserLoginForm(forms.Form):
    user = forms.CharField()
    password = forms.CharField()


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address']
