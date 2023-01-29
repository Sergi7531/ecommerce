from rest_framework.generics import ListCreateAPIView

from selling.models import Product
from selling.serializers.product import ProductsSerializer, ProductCreationSerializer


class ProductsViewSet(ListCreateAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductsSerializer
        elif self.request.method == 'POST':
            return ProductCreationSerializer

    # def get_output_serializer(self):
    # if self.request.method == 'POST':
    #     return ProductCreationSerializer
