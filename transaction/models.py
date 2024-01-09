from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count, Sum, Q
from django.db.models.functions import Coalesce


# Create your models here.
class Transaction(models.Model):
    CHARGE = 1
    PURCHASE = 2
    TRANSFER = 3

    TRANSACTION_TYPES_CHOICES = (
        (CHARGE, 'Charge'),
        (PURCHASE, 'Purchase'),
        (TRANSFER, 'Transfer')
    )
    user = models.ForeignKey(User, related_name='transactions', on_delete=models.RESTRICT)
    transaction_type = models.PositiveSmallIntegerField(choices=TRANSACTION_TYPES_CHOICES, default=CHARGE)
    amount = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.get_transaction_type_display()} -> {self.amount} Rial'

    @classmethod
    def get_report(cls):
        total_charges = Sum('transactions__amount', filter=Q(transactions__transaction_type=cls.CHARGE))
        total_purchases = Sum('transactions__amount', filter=Q(transactions__transaction_type=cls.PURCHASE))
        total_transfers = Sum('transactions__amount', filter=Q(transactions__transaction_type=cls.TRANSFER))

        users = User.objects.all().annotate(
            transactions_count=Count('transactions__id'),
            balance=Coalesce(total_charges, 0) - Coalesce(total_purchases, 0) + Coalesce(total_transfers, 0)
        )
        return users

    @classmethod
    def get_total_balance(cls, user):
        querySet = cls.get_report()
        return querySet.aggregate(Sum('balance'))


class UserBalance(models.Model):
    user = models.ForeignKey(User, related_name='balance_records', on_delete=models.RESTRICT)
    balance = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.balance} - {self.created_at}'
