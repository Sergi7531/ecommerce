
class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')

        if auth_header and auth_header.startswith('Token '):
            request.auth_token = auth_header[6:]
        else:
            request.auth_token = None

        response = self.get_response(request)
        return response
