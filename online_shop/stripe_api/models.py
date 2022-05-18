from django.db import models


class Item(models.Model):
    CURRENCY = (
        ("rub", 'RUB'),
        ("usd", 'USD'),
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY,
        default="rub",
    )

    def __str__(self):
        return (f'Item: {self.name} '
                f'Description: {self.description} '
                f'Price: {self.price} '
                f'Currency: {self.currency} ')


class Order(models.Model):
    item = models.ManyToManyField(Item)
    total_sum = models.IntegerField(default=0)
