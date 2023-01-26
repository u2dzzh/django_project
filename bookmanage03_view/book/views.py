from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def shop(request, city_id, shop_id):
    print(city_id, shop_id)
    query_parameters = request.GET
    print(query_parameters)
    return HttpResponse("dining hall")


def register(request):
    data = request.POST
    print(data)
    return HttpResponse("ok")