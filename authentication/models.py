from django.db import models


# Create your models here.
class consumer(models.Model):
    id = models.AutoField(primary_key=True)


class airConditioner(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(consumer, on_delete=models.CASCADE)
    watts = models.IntegerField()
