from rest_framework.generics import ListCreateAPIView

from selling.models import Tag
from selling.serializers.tags import TagsSerializer, TagCreationSerializer


class TagsViewSet(ListCreateAPIView):
    queryset = Tag.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TagsSerializer
        elif self.request.method == 'POST':
            return TagCreationSerializer
