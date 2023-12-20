from django.urls import re_path

from selling.views.product.add_to_cart import AddToCartView
from selling.views.product.list_create import ProductsViewSet
from selling.views.product.retrieve_update_destroy import ProductViewSet
from selling.views.shopping_cart.retrieve_update import CartViewSet
from selling.views.tags.list_create import TagsViewSet
from selling.views.tags.retrieve_update_destroy import TagViewSet

urlpatterns = [
    # Products:
    re_path(r'^products/$', ProductsViewSet.as_view(), name="list_create"),
    re_path(r'^products/(?P<product_id>[0-9_a-zA-Z\-]+)/?$', ProductViewSet.as_view(), name="retrieve_update"),

    # Tags:
    re_path(r'^tags/$', TagsViewSet.as_view(), name="list_create"),
    re_path(r'^tags/(?P<tag_id>[0-9]+)/?$', TagViewSet.as_view(), name="retrieve_update_destroy"),

    # Shopping cart:
    re_path(r'^cart/(?P<cart_id>[0-9_a-zA-Z\-]+)/?$', CartViewSet.as_view(), name="retrieve"),
    re_path(r'^cart/?$', AddToCartView.as_view(), name="add_to_cart"),

]
