from django.db import models

# Create your models here.

class Stock(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    tags = models.TextField()

    def __str__(self):
        return self.title