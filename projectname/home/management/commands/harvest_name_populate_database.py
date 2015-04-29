import random
import sys
from optparse import make_option

from django.core.management.base import BaseCommand, CommandError

from projectname.home.models import Seller, Manufacturer, Buyer
from projectname.home.harvesters import NameHarvester, ManufacturerHarvester


def progress_bar(whole, step, length=100, part=1):
        percentage = 100 * step/whole
        sys.stdout.write('\r[{0}] {1}%'.format(
            '#'*(percentage)+'-'*(length/part-percentage), percentage))
        sys.stdout.flush()


class Command(BaseCommand):
    help = 'Harvests names from the internet and creates ' \
        'Sellers, Manufacturers, Buyers'

    option_list = BaseCommand.option_list + (
        make_option(
            '--limit',
            action='store',
            dest='limit',
            default=None,
            help='Limit the results processed'),
        )

    def add_arguments(self, parser):
        parser.add_argument('limit', nargs='+', type=int)

    def handle(self, *args, **options):
        if options['limit']:
            limit = int(options['limit'])
        else:
            limit = None

        Seller.objects.all().delete()
        Buyer.objects.all().delete()
        Manufacturer.objects.all().delete()

        names = NameHarvester().harvest()
        manufacturers = ManufacturerHarvester().harvest()

        if not all([names, manufacturers]):
            raise CommandError("I can't get the names or manufacturers "
                               "from the net. Make sure youre internet "
                               "is working")
        # create the users
        sys.stdout.write("\nCreating Sellers and Buyers\n")
        whole = len(names[:limit])
        for i, obj in enumerate(names[:limit], 1):
            progress_bar(whole, i)
            Seller.objects.create(name=obj['name'])
            Buyer.objects.create(name=obj['name'])

        # create the manufacturers
        sellers = Seller.objects.values_list('id', flat=True)
        sys.stdout.write("\nCreating Manufacturers\n")
        whole = len(manufacturers[:limit])
        for i, obj in enumerate(manufacturers[:limit], 1):
            progress_bar(whole, i)
            Manufacturer.objects.create(
                name=obj['name'],
                seller=Seller.objects.get(id=random.choice(sellers))
            )
