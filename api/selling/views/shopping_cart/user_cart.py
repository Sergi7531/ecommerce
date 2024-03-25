from knox.auth import TokenAuthentication
from rest_framework.generics import RetrieveAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated

from selling.models.shopping_cart import ShoppingCart
from selling.serializers.shopping_cart import ShoppingCartSerializer


class UserCartView(RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ShoppingCartSerializer
    queryset = ShoppingCart.objects.all()

    def get_object(self):
        shopping_cart_id = self.request.user.shopping_cart.id

        return get_object_or_404(self.get_queryset(), id=shopping_cart_id)

