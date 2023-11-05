from django.db import models


# Create your models here.
class consumer(models.Model):
    id = models.EmailField(primary_key=True)
    name = models.CharField(max_length=50, null=True, default=None)
    pp = models.ImageField(upload_to="uploads", null=True, default=None)


class airConditioner(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(consumer, on_delete=models.CASCADE)
    watts = models.IntegerField()
