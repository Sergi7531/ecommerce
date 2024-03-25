from django.db.models import Q
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from common.views import HTTP_GET, HTTP_POST
from selling.models.product import Product
from selling.serializers.product import ProductsSerializer, ProductsQueryParamsSerializer, \
    ProductSerializer, ProductCreateUpdateSerializer


class ProductsViewSet(ListCreateAPIView):

    def get_serializer_class(self):
        if self.request.method == HTTP_GET:
            return ProductsSerializer
        elif self.request.method == HTTP_POST:
            return ProductCreateUpdateSerializer

    def get_queryset(self):
        serializer = ProductsQueryParamsSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)
        query_params = serializer.validated_data

        filter_params = Q()

        if query_params['name'] is not None:
            filter_params = filter_params & Q(name__icontains=query_params['name'])

        if query_params['tags'] is not None:
            tags = query_params['tags'].split(',')
            filter_params = filter_params & Q(tags__in=tags)

        if query_params['min_price'] is not None:
            filter_params = filter_params & Q(price__gte=query_params['min_price'])

        if query_params['max_price'] is not None:
            filter_params = filter_params & Q(price__lte=query_params['max_price'])

        return Product.objects.filter(filter_params)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()

        return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
