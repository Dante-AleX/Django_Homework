from django.core.management.base import BaseCommand
from myapp2.models import Product

class Command(BaseCommand):
    help = 'Creating fake product'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        num = 0.25
        for i in range(1, count + 1):
            product = Product(product_name=f'product_{i}',
                              description=f'text text {i}',
                              price=i + num,
                              product_count=10 + i)
            num += 0.25
            product.save()

