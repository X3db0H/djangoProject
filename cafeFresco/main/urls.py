from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('registration', views.registration, name="registration"),
    path('thanks', views.thanks, name="thanks"),
    path('menu', views.menu, name='menu'),
    path('about', views.about, name='about')
]