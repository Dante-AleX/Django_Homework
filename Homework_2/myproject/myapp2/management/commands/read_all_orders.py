from django.core.management.base import BaseCommand
from myapp2.models import Order


class Command(BaseCommand):
    help = 'Show all orders'

    def handle(self, *args, **kwargs):
        order = Order.objects.all()
        print(order)