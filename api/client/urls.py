from django.urls import re_path

from client.views.client.list_create import ClientsViewSet
from client.views.client.retrieve_update_destroy import EcommerceClientViewSet

urlpatterns = [
    re_path(r'^clients/$', ClientsViewSet.as_view(), name="list_create"),
    re_path(r'^clients/(?P<client_id>[0-9_a-zA-Z\-]+)/?$', EcommerceClientViewSet.as_view(), name="retrieve_update"),
]
