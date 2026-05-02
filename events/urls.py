from django.urls import path

from . import views

urlpatterns = [
    path("", views.main, name="index"),
    # ex: /events/map
    path("map", views.show_map, name="map"),
]
