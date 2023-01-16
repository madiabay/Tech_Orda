from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from accounts import models, serializers, filters


class WalletViewSet(ModelViewSet):
    queryset = models.Wallet.objects.all()
    serializer_class = serializers.WalletModelSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.WalletFilter


class AccountViewSet(ModelViewSet):
    """
    prefetch_related():
    accounts = Account.objects.all() ---> 1 sql query
    wallets = Wallet.objects.filter(account__in=accounts) ---> 1 sql query
    """
    queryset = models.Account.objects.prefetch_related(
        'wallets'
        ).all() # prefetch_related need to solve 'N + 1' problem
    serializer_class = serializers.AccountModelSerializer

# prefetch_related(): ---> prefetch_related() use 2 sql query
#     one to many
#     many to many


# select_related(): ---> select_related() use LEFT_JOIN in SQL (use only 1 sql query)
#     one to one
#     many to one
# 
# LEFT_JOIN:
# SELECT 
#     "accounts_wallet"."id",
#     "accounts_wallet"."account_id",
#     "accounts_wallet"."amount",
#     "accounts_wallet"."amount_currency",
#     "accounts_wallet"."created_at",
#     "accounts_wallet"."updated_at",
#     "accounts_account"."id",
#     "accounts_account"."first_name",
#     "accounts_account"."last_name",
#     "accounts_account"."created_at",
#     "accounts_account"."updated_at"
# FROM
#     "accounts_wallet"
# LEFT OUTER JOIN "accounts_account" ON ("accounts_wallet"."account_id" = "accounts_account"."id")