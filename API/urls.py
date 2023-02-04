from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from rest_framework_swagger.views import get_swagger_view
from .views import *



schema_view = get_schema_view(title='SQUARE SENSE - Meeting Room Occupancy API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])
schema_view = get_swagger_view(title='SQUARE SENSE - Meeting Room Occupancy API')



urlpatterns = [
    
    path('docs', schema_view, name="docs"),
    path('webhook',  webhook_listener , name="webhook_listener"),
    path('sensors',  get_sensors , name="get_sensors"),
    path('sensors/<str:sensor>/occupancy',  get_occupancy , name="get_occupancy"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
