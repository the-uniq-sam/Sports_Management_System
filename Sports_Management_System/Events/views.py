from django.shortcuts import render
from .models import event
import time
from django.utils import timezone
# Create your views here.
def Events(request):

    events = event.objects.all()

    upcoming = []
    past = []

    for i in events:
        details = {
            'event_id' : i.id,
            'event_name' : i.name,
            'organiser' : i.organiser,
            'time' : i.timestamp,
        }

        current = str(timezone.now())
        if(current<str(i.timestamp)):
            upcoming.append(details)
        else:
            past.append(details)


    context = {'uevents' : upcoming, 'pevents' : past}

    return render(request, 'Events.html', context)


def display_event(request,event_id):
    try:
        evnt = event.objects.get(pk=event_id)
    except event.DoesNotExist:
        raise Http404("Event does not exist")

    return render(request,'display.html',{'event_details': evnt})
