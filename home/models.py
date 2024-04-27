from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    image = models.ImageField()
    file = models.FileField()

