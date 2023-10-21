from django.contrib import admin

from .models import Stock, Reaction

class StockAdmin(admin.ModelAdmin):


    list_display = ('id', 'title')

admin.site.register(Stock, StockAdmin)


admin.site.register(Reaction)