from django.urls import path
from django.http import JsonResponse

def example_view(request):
    return JsonResponse({"message": "Hello from TDRS"})

urlpatterns = [
    # aquí se definen las rutas
    path('example/', example_view, name='example-view'),
]
