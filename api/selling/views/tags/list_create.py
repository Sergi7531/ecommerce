from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from common.views import HTTP_LIST_METHODS, HTTP_CREATE_METHODS
from selling.models.tag import Tag
from selling.serializers.tags import TagsSerializer, TagCreationSerializer, TagSerializer


class TagsViewSet(ListCreateAPIView):
    output_serializer_class = TagSerializer
    queryset = Tag.objects.all()

    def get_serializer_class(self):
        if self.request.method == HTTP_LIST_METHODS:
            return TagsSerializer
        elif self.request.method == HTTP_CREATE_METHODS:
            return TagCreationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()

        return Response(self.output_serializer_class(product).data, status=status.HTTP_201_CREATED)
