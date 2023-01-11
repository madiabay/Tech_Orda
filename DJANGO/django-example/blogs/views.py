# # from rest_framework import status
# # from rest_framework.views import APIView
# # from rest_framework.viewsets import ViewSet
# # from rest_framework.decorators import api_view
# # from rest_framework.response import Response
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.generics import get_object_or_404, CreateAPIView, ListAPIView

# from blogs import models, serializers


# # @api_view(['POST'])
# # def create_blog(request):
# #     serializer = serializers.BlogModelSerializer(data=request.data)
# #     serializer.is_valid(raise_exception=True)

# #     blog = models.Blog.objects.create(**serializer.validated_data)

# #     return Response(serializers.BlogModelSerializer(blog).data, status=status.HTTP_201_CREATED)


# # @api_view(['GET'])
# # def get_blog(request, *args, **kwargs):
# #     blog = get_object_or_404(models.Blog.objects.all(), **kwargs)
# #     data = serializers.BlogModelSerializer(blog).data

# #     return Response(data)


# # class BlogView(ViewSet):

# #     def list(self, request, *args, **kwargs):
# #         blogs = models.Blog.objects.all()
# #         serializer = serializers.BlogModelSerializer(blogs, many=True)

# #         return Response(serializer.data)

# #     def retrieve(self, request, pk=None, *args, **kwargs):
# #         blogs = models.Blog.objects.all()
# #         blog = get_object_or_404(blogs, pk=pk)
# #         serializer = serializers.BlogModelSerializer(blog)

# #         return Response(serializer.data)


# class BlogViewSet(ModelViewSet):

#     queryset = models.Blog.objects.all()
#     serializer_class = serializers.BlogModelSerializer





from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.response import Response

from blogs import models, serializers, services

class BlogViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    blog_services: services.BlogServicesInterface = services.BlogServicesV1()
    serializer_class = serializers.BlogModelSerializer

    def get_queryset(self):
        return models.Blog.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        self.blog_services.create_blog(serializer.validated_data)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)