from django.core.management.base import BaseCommand
from myapp2.models import Order


class Command(BaseCommand):
    help = 'Orders deleting'

    def handle(self, *args, **kwargs):
        Order.objects.all().delete()
        print('All orders have been deleted')