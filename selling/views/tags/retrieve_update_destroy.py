from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.response import Response

from selling.models import Tag
from selling.serializers.tags import TagSerializer, TagCreationSerializer


class TagViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET', 'DELETE']:
            return TagSerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return TagCreationSerializer

    def get_object(self):
        tag_id = self.kwargs.get('tag_id')
        return get_object_or_404(self.get_queryset(), id=tag_id)

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
        tag = self.get_object()
        Tag.delete(tag)

        return Response(self.get_serializer(tag).data, status=status.HTTP_200_OK)
