from multiprocessing import context

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.forms.models import model_to_dict


def index(request):
    template = loader.get_template("main/index.html")
    return HttpResponse(template.render({}, request))
