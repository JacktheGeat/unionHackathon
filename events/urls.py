from django.urls import path

from . import views

urlpatterns = [
    # ex: /events/map
    path("map", views.show_map, name="map"),
]
