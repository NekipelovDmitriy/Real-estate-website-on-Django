from django.db import models


class Listing(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square = models.DecimalField(max_digits=5, decimal_places=2)
    address = models.CharField(max_length=255)
    #image =

    def __str__(self):
        return self.title
