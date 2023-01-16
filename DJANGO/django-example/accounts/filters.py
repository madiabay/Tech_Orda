from django_filters import rest_framework as filters
from django.db.models import Q
from accounts import models


class WalletFilter(filters.FilterSet):
    first_name = filters.CharFilter('account__first_name', lookup_expr='icontains')
    last_name = filters.CharFilter('account__last_name')
    name = filters.CharFilter(method='filter_name')

    class Meta:
        model = models.Wallet
        fields = ('first_name', 'last_name', 'account')


    def filter_name(self, queryset, _, value):
        return queryset.filter(
            Q(account__first_name=value) | Q(account__last_name=value)
        )