from rest_framework.generics import CreateAPIView

from selling.serializers.shopping_cart import AddToCartSerializer


class AddToCartView(CreateAPIView):
    serializer_class = AddToCartSerializer
