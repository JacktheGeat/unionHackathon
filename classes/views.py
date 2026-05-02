from multiprocessing import context

from django.shortcuts import render

from django.http import HttpResponse
from .models import Question, Class, Building
from django.template import loader
from django.forms.models import model_to_dict

def index(request):
    classesList = Class.objects
    template = loader.get_template("classes/index.html")
    context = {"classes": classesList}
    return HttpResponse(template.render(context, request))
    
def detail(request, id):
    obj = Class.objects.get(id=id)
    classData=model_to_dict(obj)
    building = Building.objects.get(id=id)
    template = loader.get_template("classes/detail.html")
    context = {"classData": classData, "building": building}
    return HttpResponse(template.render(context, request))

def show_all(request):
    details = []
    for klass in Class.objects.iterator():
        building = klass.building
        dd = {"location": [float(building.latitude), float(building.longitude)],
              "name": klass.classname}
        details.append(dd)

    context = {"details": details}
    template = loader.get_template("classes/listAll.html")
    return render(request, 'classes/listAll.html', context)
