from django.core.management.base import BaseCommand
from myapp2.models import Order, Client, Product


class Command(BaseCommand):
    help = 'Modify your order'

    def add_arguments(self, parser):
        parser.add_argument('id_order', type=int)
        parser.add_argument('id_product', nargs='+', type=int)

    def handle(self, *args, **kwargs):
        id_order = kwargs['id_order']
        id_product = kwargs['id_product']
        order = Order.objects.get(pk=id_order)
        order.products.set(id_product)
        order.save()