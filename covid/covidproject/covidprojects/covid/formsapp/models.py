from django.db import models

# Create your models here.
class forms(models.Model):
    # place=(('Kottayam','Kottayam'),
    #        ('Alappuzha','Alappuzha'),
    #        ('kollam','Kollam'),
    #        ('ekm','ekm'),
    #        ('trivandram','trivandram'))
    name=models.CharField(max_length=150)
    Gender=models.CharField(max_length=100)
    age = models.IntegerField()
    email= models.EmailField(max_length=100)
    dob = models.DateField()
    number=models.IntegerField()
    place = models.CharField(max_length=25)
    job = models.CharField(max_length=100)
    vaccines = models.CharField(max_length=100)
    traveling = models.CharField(max_length=100)
    covidecheck = models.CharField(max_length=100)
    def __str__(self):
        return self.name