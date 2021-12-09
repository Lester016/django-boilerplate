from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.
def login_user(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        # Get form data
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Login user
            login(request, user)
            messages.success(request, f"Welcome Back {user.username}")
            return redirect("home")
        else:
            messages.error(request, "Invalid user information.")

    context = {}
    return render(request, "users/login.html", context)


def register_user(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = UserRegisterForm()  # Django Built-in views.

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get(
                "username"
            )  # cleaned_data returns a validated form.
            messages.success(
                request, f"Succesfully created user with username {username}."
            )
            login(request, user)
            return redirect("home")

    context = {"form": form}
    return render(request, "users/register.html", context)


def logout_user(request):
    logout(request)
    return redirect("login")
