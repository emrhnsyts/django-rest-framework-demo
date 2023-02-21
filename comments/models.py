import re
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Comment(models.Model):
    comment = models.TextField(max_length=100,blank=False,null=False)
    evaluation = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey('products.Product',related_name='comments',on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User',related_name='comments',on_delete=models.CASCADE,editable=False)

    def __str__(self):
        return self.comment + " " + self.product.name

