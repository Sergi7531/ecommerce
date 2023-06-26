from rest_framework.generics import RetrieveUpdateAPIView

from selling.serializers.shopping_cart import ShoppingCartSerializer


class ShoppingCartViewSet(RetrieveUpdateAPIView):

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ShoppingCartSerializer
        elif self.request.method in 