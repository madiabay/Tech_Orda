from rest_framework import serializers
from blogs import models

class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    body = serializers.CharField()


class BlogModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Blog
        fields = ('id', 'title', 'body')