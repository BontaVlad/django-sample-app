from django.db import models


class CarPartManager(models.Manager):

    def harvest_data(self, parser):
        pass


class CarPart(models.Model):
    name = models.CharField(name="Part name", max_length=255)
    price = models.DecimalField(
        name="Part price", max_digits=5, decimal_places=2)
    stock_count = models.SmallIntegerField(
        name="Number of parts in stock", default=0)
    manufacturing_date = models.DateField(name="Part manufacturing date")
    available_until = models.DateField(name="Part can be sold until")

    objects = CarPartManager()
