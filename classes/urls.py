from django.urls import path

from . import views

urlpatterns = [
    # ex: /classes/
    path("", views.index, name="index"),
    # ex: /classes/5/
    path("<int:id>/", views.detail, name="detail"),
    # ex: /classes/5/results/
    path("<int:id>/results/", views.results, name="results"),
    # ex: /classes/5/vote/
    path("<int:id>/vote/", views.vote, name="vote"),
    path("map", views.show_all, name="map"),
]
