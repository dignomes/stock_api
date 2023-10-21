import ast

from django.db import models

# Create your models here.

class Stock(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    tags = models.TextField()
    image_url = models.TextField()

    def __str__(self):
        return self.title


    def get_tags(self):
        return ast.literal_eval(self.tags)


class Reaction(models.Model):
    account = models.ForeignKey(
        "UserProfile", related_name="user_profile", on_delete=models.CASCADE
    )

    stock = models.ForeignKey(
        Stock, related_name="stock", on_delete=models.CASCADE
    )
    reaction = models.CharField(max_length=32)


class UserProfile(models.Model):

    uid = models.CharField(max_length=64)

    def __str__(self):
        return self.uid
