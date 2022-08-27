from django.db import models

from clients.models import Order

class Botlle(models.Model):

    volume = models.IntegerField(default=10)
    text = models.TextField(null=True,blank=True)
    expired = models.BooleanField(default=False)
    orders = models.ManyToManyField(
        to=Order,
        related_name='bottles',
        null=True,
        blank=True

    )

class BottlesCount(models.Model):
    bottle = models.ForeignKey(
        to=Botlle,
        related_name='bottlescount',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    count = models.IntegerField(default=0)

    order = models.ForeignKey(
        to=Order,
        related_name='bottlescount',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )