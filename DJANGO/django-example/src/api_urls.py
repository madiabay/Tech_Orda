from django.urls import path, include


urlpatterns = [
    path('v1/', include('api_urls.v1')),
    path('v2/', include('api_urls.v2')),
]
