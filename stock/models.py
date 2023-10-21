import ast

from django.db import models

# Create your models here.

class Stock(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    tags = models.TextField(null=True, blank=True)
    image_url = models.TextField(null=True, blank=True)
    ticker_symbol = models.TextField(null=True, blank=True)
    day_high = models.FloatField(null=True, blank=True)
    day_low = models.FloatField(null=True, blank=True)
    exchange = models.CharField(max_length=256, null=True, blank=True)
    fifty_day_average = models.FloatField(null=True, blank=True)
    last_price = models.FloatField(null=True, blank=True)
    last_volume = models.IntegerField(null=True, blank=True)
    market_cap = models.BigIntegerField(null=True, blank=True)
    open = models.FloatField(null=True, blank=True)
    previous_close = models.FloatField(null=True, blank=True)
    quote_type = models.CharField(max_length=256, null=True, blank=True)
    regular_market_previous_close = models.FloatField(null=True, blank=True)
    shares = models.BigIntegerField(null=True, blank=True)
    ten_day_average_volume = models.IntegerField(null=True, blank=True)
    three_month_average_volume = models.IntegerField(null=True, blank=True)
    timezone = models.CharField(max_length=256, null=True, blank=True)
    two_hundred_day_average = models.FloatField(null=True, blank=True)
    year_change = models.FloatField(null=True, blank=True)
    year_high = models.FloatField(null=True, blank=True)
    year_low = models.FloatField(null=True, blank=True)

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

    uid = models.CharField(max_length=64,unique=True)

    def __str__(self):
        return self.uid
