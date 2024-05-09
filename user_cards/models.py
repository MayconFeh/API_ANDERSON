from django.db import models
from uuid import uuid4


class CardsUser(models.Model):

    CARD_TYPE_CHOICES = (('credit', 'Crédito'), ('debit', 'Débito'),)

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey("accounts.Account", on_delete=models.CASCADE, null=False, related_name="user")
    card_type = models.CharField(max_length=10, choices=CARD_TYPE_CHOICES)
    card_number = models.CharField(max_length=16)
    exp_month = models.IntegerField()
    exp_year = models.IntegerField()
    cvc = models.CharField(max_length=4)
    is_default = models.BooleanField(default=False)
