import ast

from django.db import models

# Create your models here.

class Stock(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    tags = models.TextField()
    image_url = models.TextField()
    ticker_symbol = models.TextField()

    def __str__(self):
        return self.title


    def get_tags(self):
        return ast.literal_eval(self.tags)


    def get_stocks_by_tags(self, tags):
        result_stocks = []
        for tag in tags:
            stocks = Stock.objects.filter(tags__icontains=tag)
            for stock in stocks:
                if stock not in result_stocks:
                    result_stocks.append(stock)
        return result_stocks



class Reaction(models.Model):
    account = models.ForeignKey(
        "UserProfile", related_name="user_profile", on_delete=models.CASCADE,blank=True,
    )

    stock = models.ForeignKey(
        Stock, related_name="stock", on_delete=models.CASCADE, blank=True,
    )
    reaction = models.CharField(max_length=32)


class UserProfile(models.Model):

    uid = models.CharField(max_length=64)

    def __str__(self):
        return self.uid
