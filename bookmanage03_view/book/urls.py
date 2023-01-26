from django.urls import path

from book.views import shop, register, json

urlpatterns = [
    path('<city_id>/<shop_id>', shop),
    path('register/', register),
    path('json/', json),
]