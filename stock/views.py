import random

from django.shortcuts import render
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView, ListAPIView)

from .serializers import StockSerializer
from .models import Stock
# Create your views here.
class StockListCreateView(ListCreateAPIView):
    queryset=Stock.objects.all()
    serializer_class=StockSerializer

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)


class StockDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Stock.objects.all()
    serializer_class=StockSerializer


class StockListRandoView(ListAPIView):
    items = list(Stock.objects.all())
    queryset = random.sample(items, 10)
    serializer_class = StockSerializer