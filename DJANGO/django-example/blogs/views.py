from django.shortcuts import render

from django.http import JsonResponse
from . import models

# Create your views here.

def index(request, *args, **kwargs):
    blog = models.Blog.objects.get(id=kwargs['id'])
    blogs_titles = {
        'id': blog.id,
        'title': blog.title,
        'body': blog.body,
        }

    return JsonResponse(blogs_titles, safe=False)