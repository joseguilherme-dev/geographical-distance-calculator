from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('places_data/', views.places_dataset, name='data'),
    path('register_new_house', views.register_new_house, name='register_new_house'),
    path('delete_house/(?P<id>[0-9]+)/$', views.delete_house, name='delete_house')
]