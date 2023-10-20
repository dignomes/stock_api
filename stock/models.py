from django.db import models
from accounts.models import Account
# Create your models here.

class Stock(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    tags = models.TextField()

    def __str__(self):
        return self.title


class Reactions(models.Model):
    account = models.ForeignKey(
        Account, related_name="account", on_delete=models.CASCADE
    )

    stock = models.ForeignKey(
        "Stock", related_name="stock", on_delete=models.CASCADE
    )
    reaction = models.CharField(max_length=32)


