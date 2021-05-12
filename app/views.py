from django.http.response import HttpResponse
from django.shortcuts import render
from app.models import Service, State, City

# Create your views here.


def home(request):
    services = Service.objects.all()
    cities = City.objects.all()
    states = State.objects.all()
    context = {
        'services': services,
        'cities': cities,
        'states': states
    }
    return render(request, template_name='app/index.html', context=context)
