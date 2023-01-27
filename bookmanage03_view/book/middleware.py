from django.utils.deprecation import MiddlewareMixin

class TestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("每次请求前执行")

    def process_response(self, request, response):
        print("每次响应前执行")
        return response