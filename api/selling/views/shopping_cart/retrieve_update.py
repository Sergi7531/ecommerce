from knox.auth import TokenAuthentication
from rest_framework import status
from rest_framework.generics import get_object_or_404, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.views import HTTP_LIST_METHODS, HTTP_UPDATE_METHODS
from selling.models.shopping_cart import ShoppingCart
from selling.serializers.shopping_cart import ShoppingCartSerializer, CartUpdateSerializer


class CartViewSet(RetrieveUpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = ShoppingCart.objects.all()
    output_serializer_class = ShoppingCartSerializer

    def get_serializer_class(self):
        if self.request.method in HTTP_LIST_METHODS:
            return ShoppingCartSerializer
        elif self.request.method in HTTP_UPDATE_METHODS:
            return CartUpdateSerializer

    def get_object(self):
        shopping_cart_id = self.kwargs.get('cart_id')
        return get_object_or_404(self.get_queryset(), id=shopping_cart_id)

    def retrieve(self, request, *args, **kwargs):
        result_dict = {}
        status_code = status.HTTP_200_OK
        instance = self.get_object()
        if self.request.user.id != instance.user_id:
            status_code = status.HTTP_403_FORBIDDEN
            result_dict["errors"] = 'This shopping cart does not belong to you.'
        else:
            result_dict = self.get_serializer(instance).data

        return Response(result_dict, status_code)

    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        request.data['cart_id'] = instance.id
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)

