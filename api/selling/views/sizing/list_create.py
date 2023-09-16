from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from common.views import HTTP_LIST_METHODS, HTTP_CREATE_METHODS
from selling.models.sizing import Sizing
from selling.serializers.sizing import SizingsSerializer, SizingSerializer


class SizingsViewSet(ListCreateAPIView):
    queryset = Sizing.objects.all()

    def get_serializer_class(self):
        if self.request.method in HTTP_LIST_METHODS:
            return SizingsSerializer
        elif self.request.method in HTTP_CREATE_METHODS:
            return SizingSerializer

    def post(self, request, *args, **kwargs):
        data = {**request.data, **{'product_id': self.kwargs['product_id']}}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        sizing = serializer.save()

        return Response(self.get_serializer(sizing).data, status=status.HTTP_201_CREATED)
