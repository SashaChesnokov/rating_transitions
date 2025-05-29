from django.db import models


class Scores(models.Model):
    place = models.IntegerField(default=0)
    name = models.CharField(default='', max_length=100)
    type = models.CharField(default='', max_length=100)
    score = models.IntegerField(default=0)
    month_change = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    year_change = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    predict = models.DecimalField(default=0, max_digits=10, decimal_places=2)
