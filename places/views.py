from django.shortcuts import render
from django.views import generic, View
from django.contrib.gis.geos import fromstr, Point 
from django.contrib.gis.db.models.functions import Distance
from geopy.distance import distance as geopy_distance

from .models import Houses

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.core.serializers import serialize


# Default Location
LAT = -47.9363899
LON = -15.8293825
INSTITUTE = (-47.9363899, -15.8293825)

class Home(View):
    def get(self, request):
        houses = Houses.objects.all()

        parsed_houses = {}
        if houses:
            parsed_houses = [[house.id, house.name, round(geopy_distance(house.coords(), INSTITUTE).kilometers, 1)] for house in houses]
        
        return render(request, 'home.html', {'houses': parsed_houses})

def places_dataset(request):
    place = serialize('geojson', Houses.objects.all())
    return HttpResponse(place, content_type='json')

def register_new_house(request):
    name = request.POST.get('name')
    lat = float(request.POST.get('lat'))
    lon = float(request.POST.get('lon'))
    new_house = Houses.objects.create(name=name, location=Point(lat, lon))
    new_house.save()
    return HttpResponseRedirect(reverse('home'))
    
def delete_house(request, id=None):
    instance = Houses.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('home'))