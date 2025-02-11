from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Route for "/"
    path('home/', views.home, name='home'),  # Route for "/home"
]

# urlpatterns = [
#     path('bikes/', views.bikes, name='bikes'),
#     path('bike-components/', views.bike_components, name='bike_components'),
# ]