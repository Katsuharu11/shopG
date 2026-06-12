from django import forms
from smartshop.models import User
from django.core.exceptions import ValidationError

class UserCreateForm(forms.Form):
    user_id  = forms.CharField(label="会員ID", max_length=128, widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="パスワード", max_length=256,widget=forms.PasswordInput(render_value=True, attrs={"class": "form-control"}))
    confirm_password = forms.CharField(label="パスワード（確認）",widget=forms.PasswordInput(render_value=True, attrs={"class": "form-control"}))
    name = forms.CharField(label="名前", max_length=128, widget=forms.TextInput(attrs={"class": "form-control"}))
    address = forms.CharField(label="住所", max_length=256, widget=forms.TextInput(attrs={"class": "form-control"}))

    def clean_user_id(self):
        value = self.cleaned_data["user_id"]
        if User.objects.filter(user_id=value).exists():
            raise ValidationError("このIDは登録されています")
        return value

    def clean_password(self):
        value = self.cleaned_data["password"]
        return value

    def clean_name(self):
        value = self.cleaned_data["name"]
        return value

    def clean_address(self):
        value = self.cleaned_data["address"]
        return value
    
    

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("パスワードが一致しません")

        return cleaned_data


class UserLoginForm(forms.Form):
    user_id = forms.CharField(label="e-mail", max_length=128, widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="パスワード", max_length=256, widget=forms.PasswordInput(render_value=True, attrs={"class": "form-control"}))

    
    def clean(self):
        user_id = self.cleaned_data["user_id"]
        password = self.cleaned_data["password"]
        try:
            user = User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            raise ValidationError("登録されていないIDです")
        if user.password != password:
            raise ValidationError("パスワードが違います")
        

    

