
# Base HTTP request methods:
HTTP_GET = 'GET'
HTTP_POST = 'POST'
HTTP_PUT = 'PUT'
HTTP_PATCH = 'PATCH'
HTTP_DELETE = 'DELETE'

# Based on ViewSets, serializer class will be set with this groups of methods:
HTTP_LIST_METHODS = [HTTP_GET]
HTTP_CREATE_METHODS = [HTTP_POST]

HTTP_RETRIEVE_METHODS = [HTTP_GET, HTTP_DELETE]
HTTP_UPDATE_METHODS = [HTTP_PUT, HTTP_PATCH]
