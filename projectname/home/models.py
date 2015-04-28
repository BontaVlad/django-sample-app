from random import uniform, randrange, randint
from datetime import datetime, timedelta

from django.db import models


def random_date(start, end):
    return start + timedelta(
        seconds=randint(0, int((end - start).total_seconds())))


class CarPartManager(models.Manager):

    def make_objects(self, data, clear=True):
        if clear:
            self.get_queryset().all().delete()

        for obj in data:
            d1 = datetime.strptime('1/1/1999 1:30 PM', '%m/%d/%Y %I:%M %p')
            d2 = datetime.strptime('1/1/2017 4:50 AM', '%m/%d/%Y %I:%M %p')

            self.create(
                name=obj.get('name', 'default name'),
                price=obj.get('price', uniform(0.0, 100.0)),
                stock_count=obj.get('stock_count', randrange(100)),
                manufacturing_date=obj.get(
                    'manufacturing_date', random_date(d1, d2)),
                available_until=obj.get('available_until', random_date(d1, d2))
            )


class CarPart(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock_count = models.SmallIntegerField(default=0)
    manufacturing_date = models.DateField()
    available_until = models.DateField()

    objects = CarPartManager()
