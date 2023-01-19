from django_filters import rest_framework as filters
from django.db.models import Q, QuerySet
from accounts import models


class AccountFilter(filters.FilterSet):
    first_name = filters.CharFilter(field_name='first_name', lookup_expr='contains')
    full_name = filters.CharFilter(method='full_name_filter', lookup_expr='icontains')

    class Meta:
        model = models.Account
        fields = ('first_name', 'last_name')
    
    def full_name_filter(self, queryset: QuerySet[models.Account], _, value):
        return queryset.filter(
            Q(first_name__icontains=value) | Q(last_name__icontains=value)
        )


class WalletFilter(filters.FilterSet):
    first_name = filters.CharFilter(field_name='account__first_name', lookup_expr='icontains')
    last_name = filters.CharFilter(field_name='account__last_name')
    name = filters.CharFilter(method='filter_name')

    class Meta:
        model = models.Wallet
        fields = ('first_name', 'last_name', 'account')