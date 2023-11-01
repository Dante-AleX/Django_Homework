from django.core.management.base import BaseCommand
from myapp.models import Order


class Command(BaseCommand):
    help = 'Display all orders'

    def handle(self, *args, **kwargs):
        order = Order.objects.all()
        print(order)