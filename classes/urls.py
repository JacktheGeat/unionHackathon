from django.urls import path

from . import views

urlpatterns = [
    # ex: /classes/
    path("", views.index, name="index"),
    # ex: /classes/5/
    path("<int:id>/", views.detail, name="detail"),

    path("map", views.show_all, name="map"),
]
