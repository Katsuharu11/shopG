from django.urls import path
from . import views

app_name = "smartshop"

urlpatterns = [
    path("", views.index,name="search"),
    path("searchResult/", views.searchResult.as_view(), name="search_result"),
    path("itemDetail/<str:pk>/", views.itemDetail.as_view(), name="item_detail"),
    path("cart/", views.cart.as_view(), name="cart"),
    path("login/", views.login.as_view(), name="login"),
    path("logout/", views.logout.as_view(), name="logout"),
    path("registerUser/", views.UserCreate.as_view(), name="registerUser"),
    path("registerUserConfirm/", views.UserConfirm.as_view(), name="registerUserConfirm"),
    path("registerUserCommit/", views.UserCommit.as_view(), name="registerUserCommit"),
    path("userInfo/", views.UserInfo.as_view(), name="userInfo"),
    path("updateUser/", views.updateUser.as_view(), name="updateUser"),
    path("updateUserConfirm/", views.updateUserConfirm.as_view(), name="updateUserConfirm"),
    path("updateUserCommit/", views.updateUserCommit.as_view(), name="updateUserCommit"),
    path("withdrawConfirm/", views.withdrawConfirm.as_view(), name="withdrawConfirm"),
    path("withdrawCommit/", views.withdrawCommit.as_view(), name="withdrawCommit"),
]
