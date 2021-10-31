from django.contrib.auth import login, authenticate, get_user_model
# from django.contrib.auth.forms import UserCreationForm
# from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm


# displays Home page
def home(request):
    context = {
        "title": "Wassuup",
        "content": "This page is fully functioning on a server"
    }
    return render(request, 'home.html', context)
    # return HttpResponse("<h1>Hello world</h1>")


# Displays Contact page
def hello(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "CONTACT PAGE",
        "content": "Welcome to Contact page",
        "form": contact_form,
        "premium": "Login SUCCESSFUL. Time to do MORE!!!!"
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST)
    #     print(request.POST.get('full_name'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))

    # if request.user.is_authenticated:
        # context[" premium "] = "Login SUCCESSFUL. Time to do MORE!!!!"
    return render(request, 'index.html', context)


# Display Login page
def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("User Logged in: ", request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print("User Logged in: ", request.user.is_authenticated)
        if user is not None:
            print("User Logged in: ", request.user.is_authenticated)
            login(request, user)
            print("Success")
            # Redirect to a success page.
            # context['form'] = LoginForm()
            return redirect('/home')
        else:
            # Return an 'invalid log in' error message
            print("Not Successful. Retry Log in")
            context['form'] = LoginForm()

            # return render(request, 'auth/login.html')
    return render(request, 'auth/login.html', context)


# # Display Registration Page
# def register_page(response):
#     if response.method == 'POST':
#         form = RegisterForm(response.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login/')
#     else:
#         form = RegisterForm()
#     context = {
#         "form": form,
#         "title": "Asalaam aleikum "
#     }
#     # if form.is_valid():
#     #     # print(form.cleaned_data)
#     #     return redirect('home/')
#     return render(response, 'auth/register.html', context)


# Display Registration Page
User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print("new user is:", new_user)
    return render(request, 'auth/register.html', context)

def index0(request):
    return render(request, 'index0.html')