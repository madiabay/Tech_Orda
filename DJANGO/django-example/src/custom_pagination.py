from typing import OrderedDict
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination, CursorPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))


class CustomCursorPagination(CursorPagination):

    ordering = 'created_at'
    page_size_query_param = 'page_size'