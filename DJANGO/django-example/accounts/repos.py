from typing import OrderedDict, Protocol
from django.db.models import QuerySet, Q, F, Sum, Avg, Case, When
from django.db import transaction

from decimal import Decimal
from accounts import models, constants


class AccountReposInterface(Protocol):

    @staticmethod
    def get_accounts(action: str) -> QuerySet[models.Account]: ...

    @staticmethod
    def create_account(data: OrderedDict) -> None: ...


class AccountReposV1:

    @staticmethod
    def get_accounts(action: str) -> QuerySet[models.Account]:
        accounts = models.Account.objects.all()

        if action not in ('list', 'retrieve'):
            return accounts

        return accounts.prefetch_related(
            'wallets'
            ).annotate(
                avg_amount=Avg(
                    'wallets__amount',
                    filter=Q(wallets__amount_currency__in=(
                        constants.AmountCurrencyChoices.KZT,
                        constants.AmountCurrencyChoices.RUB,
                        constants.AmountCurrencyChoices.EUR,
                        constants.AmountCurrencyChoices.USD,
                        )),
                    default=Decimal(0.0)
                ),
                custom_amount=Sum(
                    Case(
                        When(
                            wallets__amount_currency=constants.AmountCurrencyChoices.KZT,
                            then=F('wallets__amount')*1
                        ),
                        When(
                            wallets__amount_currency=constants.AmountCurrencyChoices.RUB,
                            then=F('wallets__amount')*5
                        ),
                        When(
                            wallets__amount_currency=constants.AmountCurrencyChoices.USD,
                            then=F('wallets__amount')*450
                        ),
                        When(
                            wallets__amount_currency=constants.AmountCurrencyChoices.EUR,
                            then=F('wallets__amount')*500
                        ),
                    )
                ),
            )
    

    @staticmethod
    @transaction.atomic
    def create_account(data: OrderedDict) -> None:
        wallets = data.pop('wallets')
        # with transaction.atomic():
        account = models.Account.objects.create(**data)
        # raise AttributeError
        models.Wallet.objects.bulk_create([
            models.Wallet(**w, account=account) for w in wallets
        ])