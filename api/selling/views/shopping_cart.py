from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView, get_object_or_404
from rest_framework.response import Response

from common.views import HTTP_GET, HTTP_UPDATE_METHODS
from selling.models.shopping_cart import ShoppingCart
from selling.serializers.shopping_cart import ShoppingCartSerializer, ShoppingCartAddProductSerializer


class ShoppingCartViewSet(RetrieveUpdateAPIView):
    queryset = ShoppingCart.all_objects.all()

    input_serializer_class = ShoppingCartAddProductSerializer

    def get_serializer_class(self):
        if self.request.method == (HTTP_GET, HTTP_UPDATE_METHODS):
            return ShoppingCartSerializer

    def get_object(self):
        shopping_cart_id = self.kwargs.get('shopping_cart_id')
        return get_object_or_404(self.get_queryset(), id=shopping_cart_id)

    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)

        if partial:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)
