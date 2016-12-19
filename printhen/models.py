from django.db import models
from django.utils import timezone


class PrintHistory(models.Model):
    from_addr = models.EmailField()
    count = models.IntegerField()
