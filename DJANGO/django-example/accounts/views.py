from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from accounts import models, serializers, filters, services


# for simple router
class WalletViewSet_2(ModelViewSet):
    queryset = models.Wallet.objects.all()
    serializer_class = serializers.WalletModelSerializer_2

    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.WalletFilter




class WalletViewSet(ModelViewSet):
    # queryset = models.Wallet.objects.all()
    serializer_class = serializers.WalletModelSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.WalletFilter

    def get_serializer_context(self):
        return {'account_id': self.kwargs['account_pk']}

    def get_queryset(self):
        return models.Wallet.objects.filter(account_id=self.kwargs['account_pk'])


class AccountViewSet(ModelViewSet):
    account_services: services.AccountServicesInterface = services.AccountServicesV1()
    
    queryset = account_services.get_accounts()
    serializer_class = serializers.AccountModelSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.AccountFilter

    def perform_create(self, serializer: serializers.AccountModelSerializer):
        self.account_services.create_account(data=serializer.validated_data)