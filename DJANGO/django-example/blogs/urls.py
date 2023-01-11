from django.urls import path, include
from blogs import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', views.BlogViewSet, basename='blogs')


urlpatterns = [
    path('', include(router.urls)),
    # path('<int:id>/', views.get_blog),
    # path('', views.create_blog),
    # path('v2/', views.BlogView.as_view({'get': 'list'})),
    # path('v2/<int:pk>/', views.BlogView.as_view({'get': 'retrieve'})),
]
