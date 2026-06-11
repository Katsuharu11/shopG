from django.urls import path
from . import views

app_name = "smartshop"

urlpatterns = [
    path("", views.index),
    path("searchResult/", views.index, name="search_result"),
    path("itemDetail/", views.index, name="item_detail"),
    path("cart/", views.index, name="cart"),
    path("login/", views.index, name="login"),
    path("registerUserConfirm/", views.index, name="registerUserConfirm"),
    path("registerUserCommit/", views.index, name="registerUserCommit"),
    path("userInfo/", views.index, name="userInfo"),
    path("updateUser/", views.index, name="updateUser"),
    path("updateUserConfirm/", views.index, name="updateUserConfirm"),
    path("updateUserCommit/", views.index, name="updateUserCommit"),
    path("withdrawConfirm/", views.index, name="withdrawConfirm"),
    path("withdrawCommit/", views.index, name="withdrawCommit"),
]
