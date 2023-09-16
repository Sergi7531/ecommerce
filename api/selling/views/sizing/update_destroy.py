from rest_framework.generics import RetrieveDestroyAPIView

from common.views import HTTP_RETRIEVE_METHODS, HTTP_CREATE_METHODS
from selling.serializers.sizing import SizingSerializer


class SizingViewSet(RetrieveDestroyAPIView):

    def get_serializer_class(self):
        if self.request.method in HTTP_RETRIEVE_METHODS:
            return SizingSerializer
