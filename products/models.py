from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100,unique=True,blank=False,null=False)
    price = models.IntegerField(blank=False,null=False)
    description = models.TextField(max_length=255,null=True,blank=True)
    created_at = models.DateField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.name
