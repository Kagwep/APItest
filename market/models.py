from django.db import models

# Create your models here.

class Market(models.Model):
    name = models.CharField(max_length=200)
    description= models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='market-images')
    location = models.CharField(max_length=200)

    