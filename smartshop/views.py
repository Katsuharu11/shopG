from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
# from smartshop.models import User
# from smartshop.forms import UserCreateForm
# from smartshop.forms import UserLoginForm

def index(request):
    return render(request, "smartshop/main.html")
