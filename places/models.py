from django.db import models
from django.contrib.gis.db import models
from geopy.distance import distance as geopy_distance

# Create your models here.
class Myplaces(models.Model):
    name = models.CharField(max_length=100) #name of your place
    location = models.PointField(geography=True)

    def __str__(self):
        return self.name

    def coords(self):
        return self.location.coords