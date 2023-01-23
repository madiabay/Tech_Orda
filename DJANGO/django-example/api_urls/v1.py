from django.urls import path, include


urlpatterns = [
    path('', include('accounts.urls.v1')),
    path('', include('blogs.urls.v1')),
]