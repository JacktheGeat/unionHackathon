from django.contrib import admin

from .models import Question, Class, Building

admin.site.register(Question)

admin.site.register(Class)

admin.site.register(Building)