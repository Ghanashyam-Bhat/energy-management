from django.db import models
from authentication.models import airConditioner, consumer


# Create your models here.
class electricityUnits(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    units = models.FloatField()
    user = models.ForeignKey(consumer, on_delete=models.CASCADE)


class airConditionerUnits(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.FloatField()
    ac = models.ForeignKey(airConditioner, on_delete=models.CASCADE)


class gas(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    weight = models.FloatField()
    user = models.ForeignKey(consumer, on_delete=models.CASCADE)


class dailyHistory(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    user = models.ForeignKey(consumer, on_delete=models.CASCADE)
    totalAc = models.FloatField()
    totalElectricity = models.FloatField()
    totalGas = models.FloatField()
