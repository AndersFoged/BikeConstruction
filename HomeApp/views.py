from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'homeapp/home/index.html', {'title': 'Home'})


# def bikes(request):
#     return render(request, 'bikes.html')

# def bike_components(request):
#     return render(request, 'bike_components.html')

# def configure_bike(request):
#     return render(request, 'configure_bike.html')