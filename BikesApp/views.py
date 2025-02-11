from django.shortcuts import render, get_object_or_404, redirect
from .models import BikeModelBike, BikeType, BikeConfigurationPerBike
from ComponentsApp.models import BikeModelComponent
from BikesApp.services.bike_service_type import BikeServiceType
from BikesApp.services.bike_services import BikeServiceBike

import logging
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



logger = logging.getLogger(__name__)  # Create a logger for this module

bikeServiceBike = BikeServiceBike()

def bikes(request):
    bikes = BikeModelBike.objects.all()
    update_bike_view()
    bikes = bikeServiceBike.reverse_list(bikes)
    bike_types = {bt.id: bt.name for bt in BikeType.objects.all()}  # Create a mapping of id to name
    return render(request, 'bikesapp/bikes/bikes.html', {"bikes": bikes, "bike_types": bike_types, "title": "bikes"})


def bike_by_id(request, bike_id):
    #logger.debug("See --> Fetching bike with ID: %s", bike_id)
    update_bike_view()   
    bike = get_object_or_404(BikeModelBike, id=bike_id)
    bike_with_components = bike.components.all()
    total_price = sum(component.price for component in bike_with_components)

    bike_types = {bt.id: bt.name for bt in BikeType.objects.all()}  # Create a mapping of id to name

    return render(request, 'bikesapp/bikes/bike.html', {
        "bike_types": bike_types,
        'title': 'Bike',
        'bike': bike,
        'total_price': total_price,
        'bikeWithComponents': bike_with_components
    })


def bike_update(request, bike_id):
    bike = get_object_or_404(BikeModelBike, id=bike_id)
    bike_types = BikeType.objects.all()
    bikeComponents = BikeModelComponent.objects.all()
    selected_components = bike.components.values_list('id', flat=True)

    if request.method == 'POST':
        bike.name = request.POST['name']
        bike.description = request.POST['description']
        bike.typeId = request.POST['type']

        # Update components
        selected_ids = request.POST.getlist('selectedComponents')
        bike.components.set(selected_ids)

        bike.save()
        return redirect('bike_by_id', bike.id)

    return render(request, 'bikesapp/bikes/bike_update.html', {
        'bike': bike,
        'title': 'Update Bike',
        'bike_types': bike_types,
        'bikeComponents': bikeComponents,
        'selected_components': selected_components,
    })


def bike_create(request):
    bike_types = BikeType.objects.all()
    bikeComponents = BikeModelComponent.objects.all()

    print(f'bike_create ---> {1}')

    if request.method == 'POST':
        name = request.POST['name']
        typeId = request.POST['type']
        description = request.POST['description']

        # Create the new bike
        bike = BikeModelBike.objects.create(
            name=name,
            typeId=typeId,  # Assuming 'typeId' is a ForeignKey to BikeType
            description=description
        )

        # Update components
        selected_ids = request.POST.getlist('selectedComponents')
        bike.components.set(selected_ids)

        print(f'bike_create ---> {2}')
        bike.save()
        return redirect('bikes')

    return render(request, 'bikesapp/bikes/bike_create.html', {
        'title': 'bike Create',
        'bike_types': bike_types,
        'bikeComponents': bikeComponents,
    })

    
def delete_bike(request, bike_id):
    #print(f'delete_bike ---> {1}')
    bike = get_object_or_404(BikeModelBike, id=bike_id)
    
    # Debugging: Print related objects before deletion
    related_configs = BikeConfigurationPerBike.objects.filter(bike=bike)
    print(f"Related configurations: {list(related_configs)}")
    
    bike.delete()
    
    return redirect('bikes')


def update_bike_view():
    bikes = BikeModelBike.objects.all()
    bikeServiceType = BikeServiceType()
    bikeServiceType.get_type_color(bikes)


# def bike_create(request):
#     bike_types = BikeType.objects.all()
#     bikeComponents = BikeModelComponent.objects.all()

#     logger.debug('bike_create ---> Step 1')

#     if request.method == 'POST':
#         name = request.POST['name']
#         typeId = request.POST['type']
#         description = request.POST['description']

#         bike = BikeModelBike.objects.create(
#             name=name,
#             typeId=typeId,
#             description=description
#         )

#         selected_ids = request.POST.getlist('selectedComponents')
#         bike.components.set(selected_ids)

#         logger.debug('bike_create ---> Step 2')
#         bike.save()
#         return redirect('bikes')

#     return render(request, 'bikesapp/bikes/bike_create.html', {
#         'title': 'bike Create',
#         'bike_types': bike_types,
#         'bikeComponents': bikeComponents,
#     })

logger = logging.getLogger('django')

@csrf_exempt  # Allows JavaScript to send POST requests without CSRF issues (for development only)
def log_js_message(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            logger.info(f"JavaScript Log: {data.get('message')}")
            return JsonResponse({"status": "success"})
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)

    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)


#     print(f'bike_create ---> {1}')