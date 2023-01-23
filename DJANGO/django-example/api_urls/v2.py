from django.urls import path, include


urlpatterns = [
    path('', include('accounts.urls.v2')),
    path('', include('blogs.urls.v2')),
]