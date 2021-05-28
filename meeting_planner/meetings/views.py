from django.shortcuts import render, get_object_or_404, redirect
from .models import Meeting, Room
from django.forms import modelform_factory
# Create your views here.

def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

def showRoomObjects(request):
    rooms = Room.objects.all()
    return render(request, "meetings/rooms.html", {"rooms": rooms})

MeetingForm = modelform_factory(Meeting, exclude=[])

def new(request):
    if request.method == "POST":
        # form submitted
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome") # here welcome is name of the view function
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form":form});