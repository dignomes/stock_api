"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from stock.views import StockDetailView, StockListCreateView, ReactionViewSet,StockListRecomendView, StockByTagView

router = routers.DefaultRouter()
router.register('stock-reaction/', ReactionViewSet, basename='stock-reaction')

urlpatterns = [
    path("admin/", admin.site.urls),
    # DRF
    path("api/all-stock/", StockListCreateView.as_view(), name="all-stock"),
    path("api/stock/<int:pk>/", StockDetailView.as_view(), name="stock"),
    path('api/stock-recommend/', StockListRecomendView.as_view(), name='stock-recommend'),
    path('api/stock-by-tag/', StockByTagView.as_view(), name="stock-by-tag)"),
    path('api/', include(router.urls)),

]
