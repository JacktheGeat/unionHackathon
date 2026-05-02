from django.shortcuts import render

from django.http import HttpResponse
from .models import Event
from django.template import loader
from django.forms.models import model_to_dict

def main(request):
    return HttpResponse("test")

def show_map(request):
    details = []
    for event in Event.objects.iterator():
        dd = {"location": [float(event.latitude), float(event.longitude)],
              "name": event.name,
              "organizer": event.organizer,
              "description": event.description
              }
        if event.event_image is not None:
            dd["image_url"] = event.event_image.url

        details.append(dd)
    template = loader.get_template("events/listAll.html")
    context = {"details": details}
    return HttpResponse(template.render(context, request))
