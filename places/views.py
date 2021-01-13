from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import fromstr, Point 
from django.contrib.gis.db.models.functions import Distance
from geopy.distance import distance as geopy_distance

from .models import Myplaces

from django.http import HttpResponse

from django.core.serializers import serialize


# Default Location
latitude = -47.9363899
longitude = -15.8293825
institute = (-47.9363899, -15.8293825)

class Home(generic.ListView):
    model = Myplaces
    
    queryset = Myplaces.objects.all()

    new_queryset = [[query.name, round(geopy_distance(query.coords(), institute).kilometers, 1)] for query in queryset]
    
    queryset = new_queryset

    context_object_name = 'people'

    template_name = 'home.html'

def places_dataset(request):
    place = serialize('geojson', Myplaces.objects.all())

    return HttpResponse(place, content_type='json')