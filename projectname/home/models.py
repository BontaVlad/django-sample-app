from random import uniform, randrange, randint, choice
from datetime import datetime, timedelta

from django.db import models

import pprofile

profiler = pprofile.Profile()


def random_date(start, end):
    with profiler:
        return start + timedelta(
            seconds=randint(0, int((end - start).total_seconds())))


class CarPartManager(models.Manager):

    def make_objects(self, data, clear=True):
        # maybe we want to start fresh
        if clear:
            self.get_queryset().all().delete()

        # we just need the id's
        buyers = Buyer.objects.values_list('id', flat=True)
        manufacturers = Manufacturer.objects.values_list('id', flat=True)

        # make sure we have something to work with
        if not all([buyers, manufacturers]):
            raise ValueError("You don't have any buyers or manufacturers,"
                             "make sure you run"
                             "./manage.py harvest_name_and_populate_database "
                             "in the console")

        for obj in data:
            d1 = datetime.strptime('1/1/1999 1:30 PM', '%m/%d/%Y %I:%M %p')
            d2 = datetime.strptime('1/1/2017 4:50 AM', '%m/%d/%Y %I:%M %p')

            # handle obj in a more polimorphic way
            self.create(
                buyer=Buyer.objects.get(id=choice(buyers)),
                manufacturer=Manufacturer.objects.get(
                    id=choice(manufacturers)),
                name=obj.get('name', 'default name'),
                price=obj.get('price', uniform(0.0, 100.0)),
                stock_count=obj.get('stock_count', randrange(100)),
                manufacturing_date=obj.get(
                    'manufacturing_date', random_date(d1, d2)),
                available_until=obj.get('available_until', random_date(d1, d2))
            )


class Seller(models.Model):
    name = models.CharField(max_length=255)


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    seller = models.ForeignKey(Seller)


class Buyer(models.Model):
    name = models.CharField(max_length=255)


class CarPart(models.Model):
    manufacturer = models.ForeignKey(Manufacturer)
    buyer = models.ForeignKey(Buyer, null=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock_count = models.SmallIntegerField(default=0)
    manufacturing_date = models.DateField()
    available_until = models.DateField()

    objects = CarPartManager()
