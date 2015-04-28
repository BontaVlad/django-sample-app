from datetime import datetime

from django.db import models


class CarPartManager(models.Manager):

    def make_objects(self, data, clear=True):
        if clear:
            self.get_queryset().all().delete()

        for obj in data:
            self.create(
                name=obj.get('name', 'default name'),
                price=obj.get('price', 0.0),
                stock_count=obj.get('stock_count', 0),
                manufacturing_date=obj.get(
                    'manufacturing_date', datetime.now()),
                available_until=obj.get('available_until', datetime.now())
            )


class CarPart(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock_count = models.SmallIntegerField(default=0)
    manufacturing_date = models.DateField()
    available_until = models.DateField()

    objects = CarPartManager()
