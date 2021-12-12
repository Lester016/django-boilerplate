from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
def home(request):
    users = User.objects.all()

    context = {"users": users}
    return render(request, "main/home.html", context)
