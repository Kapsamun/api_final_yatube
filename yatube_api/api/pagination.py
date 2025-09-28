from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

    def get_paginated_response(self, data):
        return Response({
            'count': self.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })

class ConditionalPagination(CustomLimitOffsetPagination):
    def paginate_queryset(self, queryset, request, view=None):
        if not (request.query_params.get('limit') or request.query_params.get('offset')):
            return None
        return super().paginate_queryset(queryset, request, view)
