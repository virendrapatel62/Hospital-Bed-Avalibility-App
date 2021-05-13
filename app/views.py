from django.http.response import HttpResponse
from django.shortcuts import render
from app.models import Facility, State, City

# Create your views here.


def home(request):
    facilities = Facility.objects.all()
    cities = City.objects.all()
    states = State.objects.all()
    context = {
        'facilities': facilities,
        'cities': cities,
        'states': states
    }
    return render(request, template_name='app/index.html', context=context)
