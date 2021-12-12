from django.db import models

# Create your models here.
from django.urls import reverse


class Place(models.Model):
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=500)
    phone=models.IntegerField()
    address=models.CharField(max_length=250)
    site=models.URLField()
    slug=models.SlugField(max_length=100,unique=True)

    def __str__(self):
       return  self.name
    def get_url(self):
        return reverse('covidapp:getplace',args=[self.slug])