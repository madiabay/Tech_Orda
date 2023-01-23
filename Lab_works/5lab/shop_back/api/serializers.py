from rest_framework import serializers
from api import models


class ProductModelSerializer_2(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = "__all__"




class ProductModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = "__all__"
    
    def create(self, validated_data):
        category_id = self.context['category_id']
        return models.Product.objects.create(category_id=category_id, **validated_data)


class CategoryModelSerializer(serializers.ModelSerializer):

    products = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = models.Category
        fields = "__all__"