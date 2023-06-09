from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from selling.models import Tag


class TagCreationSerializer(ModelSerializer):
    related_tags = CharField()

    class Meta:
        model = Tag
        fields = ('name', 'relevance', 'related_tags')


class TagsSerializer(ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name', 'relevance')


class TagSerializer(ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name', 'relevance', 'related_tags')
