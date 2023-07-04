from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from client.models import EcommerceClient
from client.serializers.client import EcommerceClientsSerializer, EcommerceClientCreationSerializer


class ClientsViewSet(ListCreateAPIView):
    queryset = EcommerceClient.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return EcommerceClientCreationSerializer
        elif self.request.method == 'GET':
            return EcommerceClientsSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(EcommerceClientsSerializer(serializer.data).data, status=status.HTTP_201_CREATED)
