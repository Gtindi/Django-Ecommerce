from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    fullName = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Content"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if "gmail.com" not in email:
            raise forms.ValidationError("Email must be gmail.")
        return email


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))
    # fields = ['username', 'password']


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Password"
            }))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": "Enter Password"
        }
    ))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken my nigger!!")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is taken my nigger!!")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("Password must match!")

        return data

# class RegisterForm(UserCreationForm):
#     email = forms.EmailField()
    # class Meta:
    #     model = User
    #     fields = ["username", "email", "password1", "password2"]
