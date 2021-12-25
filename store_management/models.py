from django.db import models

# Create your models here.
class Stores(models.Model):
    name= models.CharField(max_length=255)
    code= models.CharField(max_length=255)
    active= models.IntegerField()
    created_at= models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at= models.DateTimeField(blank=True, null=True, auto_now=True)
    quantity= models.IntegerField()
    type= models.CharField(max_length=255)
    gst= models.DecimalField(max_digits=5, decimal_places=2)
    price= models.IntegerField()
    class Meta:
        managed=True
        db_table='stores'