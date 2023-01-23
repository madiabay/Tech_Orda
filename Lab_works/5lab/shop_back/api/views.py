from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from api import models, serializers


# @api_view(['GET'])
# def get_product(request, **kwargs):
#     product = get_object_or_404(models.Product.objects.all(), **kwargs)
#     serializer = serializers.ProductModelSerializer(product)

#     return Response(serializer.data)

# @api_view(['GET'])
# def get_products(request):
#     products = models.Product.objects.all()
#     serializer = serializers.ProductModelSerializer(products, many=True)

#     return Response(serializer.data)

# @api_view(['POST'])
# def create_product(request):
#     serializer = serializers.ProductModelSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)

#     models.Product.objects.create(**serializer.validated_data)
#     return Response(serializer.data, status=status.HTTP_201_CREATED)



# class ProductView(APIView):

#     def get(self, request, *args, **kwargs):

#         product = models.Product.objects.all()
#         serializer = serializers.ProductModelSerializer(product, many=True)

#         return Response(serializer.data)


# class ProductView(ViewSet):

#     def list(self, request):
#         products = models.Product.objects.all()
#         serializer = serializers.ProductModelSerializer(products, many=True)

#         return Response(serializer.data)
    
#     def retrieve(self, request, pk=None):
#         products = models.Product.objects.all()
#         product = get_object_or_404(products, pk=pk)
#         serializer = serializers.ProductModelSerializer(product)
#         return Response(serializer.data)


class ProductViewSet(ModelViewSet):

    serializer_class = serializers.ProductModelSerializer

    def get_serializer_context(self):
        return {'category_id': self.kwargs['category_pk']}
    
    def get_queryset(self):
        return models.Product.objects.filter(category_id=self.kwargs['category_pk'])


class CategoryViewSet(ModelViewSet):

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoryModelSerializer




class ProductViewSet_2(ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductModelSerializer_2