from rest_framework import serializers
from accounts import models


class WalletModelSerializer(serializers.ModelSerializer):
    # account = AccountModelSerializer(read_only=True, allow_null=True)

    # account = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = models.Wallet
        fields = "__all__"


class _WalletModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Wallet
        fields = (
            'id',
            'amount',
            'amount_currency',
        )


class AccountModelSerializer(serializers.ModelSerializer):
    wallets = _WalletModelSerializer(read_only=True, many=True)

    # wallets = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = models.Account
        fields = "__all__" # (
        #     'id',
        #     'first_name',
        #     'last_name',
        #     'created_at',
        #     'updated_at',
        #     'wallets',
        # )

