from currency.models import RequestResponseLog
from time import time


class RequestResponseLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time()

        response = self.get_response(request)

        finish_time = time()
        RequestResponseLog(path=request.path, request_method=request.method, time=finish_time - start_time).save()

        return response
