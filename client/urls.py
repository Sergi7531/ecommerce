from django.urls import re_path

from client.views.client.list_create import ClientsViewSet
from client.views.client.retrieve_update_destroy import ClientViewSet
from selling.views.product.list_create import ProductsViewSet
from selling.views.product.retrieve_update_destroy import ProductViewSet

urlpatterns = [
    re_path(r'^clients/$', ClientsViewSet.as_view(), name="list_create"),
    re_path(r'^clients/(?P<client_id>[0-9_a-zA-Z\-]+)/?$', ClientViewSet.as_view(), name="retrieve_update"),
]
