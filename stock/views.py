import random

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, GenericAPIView)
from rest_framework.request import Request
from rest_framework.response import Response

from .data.reactions import ReactionService
from .serializers import StockSerializer
from .models import Stock
from .services.recomendation_module import RecomendationSystem


# Create your views here.
class StockListCreateView(ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class StockDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockListRecomendView(GenericAPIView):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()

    def get(self, request: Request, *args, **kwargs):
        account_id = request.META.get("X-User-GUID")
        return Response([self.serializer_class(i).data for i in RecomendationSystem().get_recommendation(account_id)])


class ReactionViewSet(viewsets.ViewSet):
    def create(self, request: Request) -> Response:
        stock_id = request.data.get("stockId")
        account_id = request.data.get("accountId")
        reaction = request.data.get("reaction")
        ReactionService().create_reaction(account_id, stock_id, reaction)
        return Response(status=status.HTTP_204_NO_CONTENT)

# {"stockId":158,
#  "accountId":"1",
#  "reaction":"LIKE"
#  }

