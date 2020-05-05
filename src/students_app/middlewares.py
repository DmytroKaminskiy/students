from time import time


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):

        if request.path.startswith('/admin/'):
            start = time()
            response = self.get_response(request)  # view
            end = time()
            print(end - start)
        else:
            response = self.get_response(request)  # view

        return response
