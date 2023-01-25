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


# V1
class AccountViewSet(ModelViewSet):
    account_services: services.AccountServicesInterface = services.AccountServicesV1()
    
    # queryset = account_services.get_accounts()
    serializer_class = serializers.RetrieveAccountModelSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.AccountFilter

    def get_queryset(self):
        return self.account_services.get_accounts(self.action)

    # def perform_create(self, serializer: serializers.AccountModelSerializer):
    #     self.account_services.create_account(data=serializer.validated_data)


# # V2
# class AccountViewSetV2(ModelViewSet):
#     account_services: services.AccountServicesInterface = services.AccountServicesV1()
    
#     queryset = account_services.get_accounts()
#     serializer_class = serializers.AccountModelSerializerV2

#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = filters.AccountFilter

#     def perform_create(self, serializer: serializers.AccountModelSerializer):
#         self.account_services.create_account(data=serializer.validated_data)


class AccountViewSetV2(ModelViewSet):
    account_services: services.AccountServicesInterface = services.AccountServicesV1()
    
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.AccountFilter

    def get_queryset(self):
        return self.account_services.get_accounts(action=self.action)

    def get_serializer_class(self):

        print(f'{self.action=}')

        if self.action in ('list', 'retrieve'):
            return serializers.RetrieveAccountModelSerializer
        
        return serializers.CreateAccountModelSerializer

    def perform_create(self, serializer: serializers.CreateAccountModelSerializer):
        self.account_services.create_account(data=serializer.validated_data)