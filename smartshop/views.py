from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from smartshop.models import Item,Category
# from smartshop.forms import UserCreateForm
# from smartshop.forms import UserLoginForm

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
        
        return