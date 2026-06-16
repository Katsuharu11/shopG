from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from smartshop.models import Item,Category,User,ShoppingCart
from smartshop.forms import UserCreateForm
from smartshop.forms import UserLoginForm
from smartshop.forms import UserUpdateForm

def index(request):
    return render(request, "smartshop/main.html")

class searchResult(View):

    def get(self, request, *args, **kwargs):
        pass #直接来た場合は後で考える

    

    def post(self, request, *args, **kwargs):
        category_val = request.POST.get('category')      # カテゴリ
        keyword = request.POST.get('keyword')  # キーワード

        # 初期：全件取得
        items = Item.objects.all()

        # カテゴリ条件（F = すべて）
        if category_val != 'All':
            items=items.filter(category=category_val)
            category_name=Category.objects.get(category_id=category_val).name
        else:
            items=items
            category_name="すべて"

        items = items.filter(name__icontains=keyword)

        # キーワード条件（商品名に含む）
        context={
            "items":items,
            "category":category_name,
            "keyword":keyword,
        }

        return render(request, 'smartshop/searchResult.html', context)
    
class searchResult(View):

    def get(self, request, *args, **kwargs):
        pass #直接来た場合は後で考える

    

    def post(self, request, *args, **kwargs):
        category_val = request.POST.get('category')      # カテゴリ
        keyword = request.POST.get('keyword')  # キーワード

        # 初期：全件取得
        items = Item.objects.all()

        # カテゴリ条件（F = すべて）
        if category_val != 'All':
            items=items.filter(category=category_val)
            category_name=Category.objects.get(category_id=category_val).name
        else:
            items=items
            category_name="すべて"

        items = items.filter(name__icontains=keyword)

        # キーワード条件（商品名に含む）
        context={
            "items":items,
            "category":category_name,
            "keyword":keyword,
        }

        return render(request, 'smartshop/searchResult.html', context)
    




class itemDetail(View):

    def get(self, request, pk, *args, **kwargs):
        queryset = Item.objects.get(name=pk)
        context = {
            "items": queryset,
            "stock_list": range(1, queryset.stock + 1),
            }
        return render(request, "smartshop/itemDetail.html", context)

class cart(View):
    def get(self, request, *args, **kwargs):
        if "user_id" not in request.session:
            return redirect("smartshop:login")

        user_id=request.session["user_id"]
        user_cart=ShoppingCart.objects.filter(user_id=user_id)
        total_price = 0
        for cart in user_cart:
            total_price += cart.item.price * cart.amount


        context = {
            "user_cart":user_cart,
            "total_price":total_price,
        }
        return render(request, "smartshop/cart.html", context)
    
    def post(self, request, *args, **kwargs):
        if "user_id" not in request.session:
            return redirect("smartshop:login")


        cart = ShoppingCart()
        buy_amount = int(request.POST.get('amount'))
        item_id = int(request.POST.get("item_id"))


        
        user_id=request.session["user_id"]
        user=User.objects.get(user_id=user_id)
        item=Item.objects.get(item_id=item_id)

        cart.amount=buy_amount
        cart.item =item
        cart.user= user
        cart.save()
        
    
        user_cart=ShoppingCart.objects.filter(user=user)

        total_price = 0
        for cart in user_cart:
            total_price += cart.item.price * cart.amount


        context = {
            "user_cart":user_cart,
            "total_price":total_price,
        }
        return render(request, "smartshop/cart.html", context)
    

    
class UserCreate(View):

    def get(self, request, *args, **kwargs):
        form = UserCreateForm()
        context = {
            "form": form,
        }
        return render(request, "smartshop/registUser.html", context)

    

    def post(self, request, *args, **kwargs):
       pass
  
class UserConfirm(View):

    def get(self, request, *args, **kwargs):
        pass

    

    def post(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        queryset = User.objects.all().order_by("-user_id")
        context={
           "user_list":queryset
        }

        if not form.is_valid():  # バリデーション実施、問題があった場合の処理
            context = {
                "form": form,
                "user_list": queryset,
            }
            return render(request, "smartshop/registUser.html", context)

        new_user = User()
        # バリデーションに問題がなかったデータの取り出しDepartmentモデルにセット
        new_user.password = form.cleaned_data.get("password")
        new_user.name = form.cleaned_data.get("name")
        new_user.user_id = form.cleaned_data.get("user_id")
        new_user.address = form.cleaned_data.get("address")
        # new_user.save()
        # department_listビューの呼び出し
        context={
            "new_user":new_user
        }
        return render(request, "smartshop/registUserConfirm.html", context)
    
class UserCommit(View):

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        new_user = User()
        # バリデーションに問題がなかったデータの取り出しDepartmentモデルにセット
        new_user.password = request.POST.get("password")
        new_user.name = request.POST.get("name")
        new_user.user_id = request.POST.get("user_id")
        new_user.address = request.POST.get("address")
        new_user.save()

        context={
            "user_name":new_user.name
        }

        return render(request, "smartshop/registUserCommit.html",context)
    
class login(View):

    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        context = {
            "form": form,
        }
        return render(request, "smartshop/login.html", context)

    

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data["user_id"]
            user = User.objects.get(user_id=user_id)
            name=user.name
            request.session["name"] = name
            request.session["user_id"] = user_id

            return redirect("smartshop:search")
        context = {
            "form": form,
            }
        return render(request, "smartshop/login.html", context)
    
class logout(View):

    def get(self, request, *args, **kwargs):
        request.session.flush()
        return redirect("smartshop:login")

    

    def post(self, request, *args, **kwargs):
       pass

class UserInfo(View):

    def get(self, request, *args, **kwargs):
        user_id= request.session["user_id"]
        user = User.objects.get(user_id=user_id)
        context = {
            "user": user,
            }
        return render(request, "smartshop/userInfo.html", context)


    def post(self, request, *args, **kwargs):
        pass

class updateUser(View):

    def get(self, request, *args, **kwargs):
        form = UserUpdateForm()
        user_id= request.session["user_id"]
        user = User.objects.get(user_id=user_id)
        context = {
            "form": form,
            "user": user,
        }
        return render(request, "smartshop/updateUser.html", context)
    
class updateUserConfirm(View):

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        form = UserUpdateForm(request.POST)

        user_id = request.session["user_id"]
        user = User.objects.get(user_id=user_id)

        if not form.is_valid():
            context = {
                "form": form,
                "user": user,
            }
            return render(request, "smartshop/updateUser.html", context)

        new_password = form.cleaned_data.get("password")

        context = {
            "user": user,
            "new_password": new_password,
        }

        return render(request, "smartshop/updateUserConfirm.html", context)
    
class updateUserCommit(View):

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        new_user = User()

        new_user.password = request.POST.get("password")
        new_user.name = request.POST.get("name")
        new_user.user_id = request.POST.get("user_id")
        new_user.address = request.POST.get("address")
        new_user.save()

        context={
            "user":new_user
        }

        return render(request, "smartshop/updateUserCommit.html",context)
    
class withdrawConfirm(View):

    def get(self, request, *args, **kwargs):
        name=request.session["name"]

        context={
            "name":name
        }

        return render(request, "smartshop/withdrawConfirm.html",context)

    def post(self, request, *args, **kwargs):
        pass
    
class withdrawCommit(View):

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        user_id = request.session["user_id"]
        name=request.session["name"]
        user = User.objects.get(user_id=user_id)
        user.delete()
        request.session.flush()

        context={
            "name":name
        }

        return render(request, "smartshop/withdrawCommit.html",context)


