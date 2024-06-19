from django.db import models

# Create your models here.


class ELS_PRODUCT(models.Model):
    name = models.CharField(max_length=200)
    value = models.IntegerField()