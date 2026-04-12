from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cars/')

    def __str__(self):
        return self.name