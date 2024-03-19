import json
from functools import wraps

def authorized_test(func):
    @wraps(func)
    def wrapper(self, api_client, *args, **kwargs):
        response = api_client.post(self._login_url, data={"email": 'test123456789@example.com',
                                                           "password": 'testing_password123'})

        api_client.credentials(HTTP_AUTHORIZATION=f'Token {json.loads(response.content)["token"]}')
        return func(self, api_client, *args, **kwargs)
    return wrapper
