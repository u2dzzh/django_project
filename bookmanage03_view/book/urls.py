from django.urls import path

from book.views import shop, register

urlpatterns = [
    path('<city_id>/<shop_id>', shop),
    path('register/', register),
]