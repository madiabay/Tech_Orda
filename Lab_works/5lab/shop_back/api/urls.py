from django.urls import path, include
from api import views
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('products', views.ProductViewSet_2)
router.register('products', views.ProductViewSet, basename='category-products')
router.register('categories', views.CategoryViewSet)

category_router = routers.NestedDefaultRouter(router, 'categories', lookup='category')
category_router.register('products', views.ProductViewSet, basename='category-products')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(category_router.urls)),
]

# urlpatterns = [
#     path('', include(router.urls)),
#     # path('<int:id>/', views.get_product), # @api_view
#     # path('', views.get_products), # @api_view
#     # # path('v2/', views.ProductView.as_view()), # APIView
#     # path('v2/', views.ProductView.as_view({'get': 'list'})), # ViewSet
#     # path('v2/<int:pk>/', views.ProductView.as_view({'get': 'retrieve'})), # ViewSet
#     # path('create', views.create_product), # @api_view
# ]
