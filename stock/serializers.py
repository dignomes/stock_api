from rest_framework import serializers
from .models import Stock


class StockSerializer(serializers.ModelSerializer):
    stock=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Stock
        fields='__all__'