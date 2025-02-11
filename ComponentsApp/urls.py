from django.urls import path
from ComponentsApp import views
from .views import component_update, log_js_message, component_create, components, component_delete

urlpatterns = [
    path('', views.components, name='components'),  # Empty path instead of 'components/'
    path('components/', components, name='components'),
    path('component_create', component_create, name='component_create'),
    path('component_update/<int:component_id>/', component_update, name='component_update'),
    path('component_delete/<int:component_id>/', component_delete, name='component_delete'),

    path("log_js/", log_js_message, name="log_js_message"),
]