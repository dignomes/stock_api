import csv
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django.setup()
from stock.models import Stock

def populate_stock_model():
    file_name = 'stock/data.csv'
    input_file = csv.DictReader(open(file_name))
    for row in input_file:
        stock = Stock.objects.create(title=row['company_name'], description=row['description'], tags=row['tags'])
        stock.save()

    return

if __name__ == "__main__":
    populate_stock_model()