from django.shortcuts import render, redirect 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import json
import logging

from .models import BikeModelComponent

def components(request):
    components = BikeModelComponent.objects.all()
    return render(request, 'componentsapp/components/components.html', {"components":components ,'title': 'components'})   
    


@csrf_exempt
def component_create(request):
    if request.method == 'POST':
        try:
            # Check if request body exists
            if not request.body:
                return JsonResponse({'success': False, 'message': 'No data received'}, status=400)

            data = json.loads(request.body)
            print(f'Incoming data: {data}')  # Debugging

            # Extract values
            name = data.get('name')
            description = data.get('description')
            category = data.get('category')
            price = data.get('price')
            price = price.replace(',', '.')

            # Validate required fields
            if not all([name, description, category, price]):
                return JsonResponse({'success': False, 'message': 'Missing required fields'}, status=400)

            # Create and save the component
            component = BikeModelComponent.objects.create(
                name=name,
                description=description,
                category=category,
                price=price
            )

            return JsonResponse({'success': True, 'message': 'Component created successfully!'})

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON format'}, status=400)
        except Exception as e:
            print(f'Error in component_create: {e}')  # Debugging
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=400)


@csrf_exempt
def component_update(request, component_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            description = data.get('description')
            category = data.get('category')
            price = data.get('price')

            # Assuming the component exists and is fetched from the database
            component = BikeModelComponent.objects.get(id=component_id)

            # Update the component details
            component.name = name
            component.description = description
            component.category = category
            component.price = price

            component.save()

            return JsonResponse({
                'success': True,
                'name': name,
                'description': description,
                'category': category,
                'price': price
            })
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=400)


@csrf_exempt
def component_delete(request,component_id):
    print(f"Related configurations: --> {component_id}")

    component = BikeModelComponent.objects.get(id=component_id)
    
   
    print(f"Related configurations: 1 --> {component}")
    
    component.delete()
    print(f"Related configurations: 1 --> {'delete'}")
    return redirect('components')




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

logger = logging.getLogger(__name__)

#     print(f'component_create ---> {1}')