from django.urls import path, include
from blogs import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('blogs', views.BlogViewSet, basename='blogs')


urlpatterns = [
    path('', include(router.urls)),
]