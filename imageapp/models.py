from django.db import models

# Create your models here.
class product(models.Model):
    product_name=models.CharField(max_length=100,null=True)
    price=models.IntegerField()
    quantity=models.IntegerField()
    image=models.ImageField(upload_to="image/",null=True)