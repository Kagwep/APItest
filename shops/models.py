from django.db import models

# Create your models here.

class Shops(models.Model):
    name = models.CharField(max_length=200)
    description= models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='shop-images')
    website = models.CharField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=200)
    area_code = models.IntegerField()
    code = models.CharField(max_length=100)
    
    
    