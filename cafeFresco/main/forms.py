
from django.forms import ModelForm, TextInput, PasswordInput
from .models import Reg


class RegForm(ModelForm):
    class Meta:
        model = Reg
        fields = ['login', 'password', 'name', 'surname', 'mail']

        widgets = {
            "login": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин',
            }),
            "password": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "mail": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта'
            }),
        }
