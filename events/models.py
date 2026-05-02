from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    latitude = models.FloatField(max_length=100)
    longitude = models.FloatField(max_length=100)
    eventDate = models.DateTimeField("Start Date")
    endDate = models.DateTimeField("End Date")
    event_image = models.ImageField(null=True, upload_to="event_images")
    def __str__(self):
        return self.name
