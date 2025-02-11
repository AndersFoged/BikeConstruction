from django.urls import path
from . import views
from .views import bike_by_id, bike_update, bike_create, delete_bike, log_js_message

urlpatterns = [
    path('', views.bikes, name='bikes'),
    path('bikes/bike/<int:bike_id>/', bike_by_id, name='bike_by_id'),
    path('bike/bike_update/<int:bike_id>/', bike_update, name='bike_update'),
    path('bike/bike_create', bike_create, name='bike_create'),
    path('bike/delete_bike/<int:bike_id>/', delete_bike, name='delete_bike'),

    path("log_js/", log_js_message, name="log_js_message"),
]