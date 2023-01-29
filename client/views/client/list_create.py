from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from client.models import Client
from client.serializers.client import ClientsSerializer, ClientCreationSerializer


class ClientsViewSet(ListCreateAPIView):
    queryset = Client.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ClientCreationSerializer
        elif self.request.method == 'GET':
            return ClientsSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(ClientsSerializer(serializer.data).data, status=status.HTTP_201_CREATED)
