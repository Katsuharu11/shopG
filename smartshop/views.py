from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from smartshop.models import Item,Category,User
from smartshop.forms import UserCreateForm
from smartshop.forms import UserLoginForm

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
    def post(self, request, *args, **kwargs):
        buy_amount=int(request.POST.get('amount'))
        item_id=int(request.POST.get("items_id"))
        queryset = Item.objects.get(item_id=item_id)
        context = {
            "items": queryset,
            "amount":buy_amount,
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
        #入力したものの検証
        #OKならUserConfirmに値を渡す
        pass
        # new_user.save()
        # # department_listビューの呼び出し
        # return render(request, "smartshop/registUser.html", context)
  
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
        if not form.is_valid():  # バリデーション実施、問題があった場合の処理
            context = {
                "form": form,
            }
        return redirect("smartshop:search")
