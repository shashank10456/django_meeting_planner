from django.contrib import admin
from .models import Meeting, Room #import model class


# Register your models here. This is required to be able to use admin interface with the app
admin.site.register(Meeting)
admin.site.register(Room)