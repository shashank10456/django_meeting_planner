from django.db import models
from datetime import time
# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=200)
    floor_number = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.name} is on floor number {self.floor_number} and has room number as {self.room_number}"

class Meeting(models.Model):
    # inherit base class->makes official django model and starts representing tables
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"
