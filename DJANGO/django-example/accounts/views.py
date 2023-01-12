from rest_framework.viewsets import ModelViewSet
from accounts import models, serializers


class WalletViewSet(ModelViewSet):
    queryset = models.Wallet.objects.all()
    serializer_class = serializers.WalletModelSerializer


class AccountViewSet(ModelViewSet):
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountModelSerializer