from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.response import Response

from selling.models import Product
from selling.serializers.product import ProductSerializer, ProductUpdateSerializer


class ProductViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET', 'DELETE']:
            return ProductSerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return ProductUpdateSerializer

    def get_object(self):
        product_id = self.kwargs.get('product_id')
        return get_object_or_404(self.get_queryset(), id=product_id)

    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        product = self.get_object()
        Product.delete(product)

        return Response(self.get_serializer(product).data, status=status.HTTP_200_OK)
