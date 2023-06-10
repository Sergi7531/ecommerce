from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.response import Response

from client.models import Client
from client.serializers.client import ClientSerializer, ClientCreationSerializer


class ClientViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET', 'DELETE']:
            return ClientSerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return ClientCreationSerializer

    def get_object(self):
        client_id = self.kwargs.get('client_id')
        return get_object_or_404(self.get_queryset(), id=client_id)

    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(self.get_serializer(instance).data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        client = self.get_object()
        Client.delete(client)

        return Response(self.get_serializer(client).data, status=status.HTTP_200_OK)
