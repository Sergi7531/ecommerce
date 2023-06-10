from rest_framework.serializers import ModelSerializer

from selling.models import Tag


class TagsSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'relevance')


class TagCreationSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', 'relevance', 'related_tags')


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'relevance', 'related_tags')
