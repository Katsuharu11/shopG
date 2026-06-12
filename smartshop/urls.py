from django.urls import path
from . import views

app_name = "smartshop"

urlpatterns = [
    path("", views.index,name="search"),
    path("searchResult/", views.searchResult.as_view(), name="search_result"),
    path("itemDetail/<str:pk>/", views.itemDetail.as_view(), name="item_detail"),
    path("cart/", views.index, name="cart"),
    path("login/", views.login.as_view(), name="login"),
    path("registerUser/", views.UserCreate.as_view(), name="registerUser"),
    path("registerUserConfirm/", views.UserConfirm.as_view(), name="registerUserConfirm"),
    path("registerUserCommit/", views.UserCommit.as_view(), name="registerUserCommit"),
    path("userInfo/", views.index, name="userInfo"),
    path("updateUser/", views.index, name="updateUser"),
    path("updateUserConfirm/", views.index, name="updateUserConfirm"),
    path("updateUserCommit/", views.index, name="updateUserCommit"),
    path("withdrawConfirm/", views.index, name="withdrawConfirm"),
    path("withdrawCommit/", views.index, name="withdrawCommit"),
]
