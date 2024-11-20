from django.urls import path
from .views import LicitacionListView, TDRListView, LicitacionCreateView, LicitacionUpdateView, LicitacionDeleteView, LicitacionDetailView

urlpatterns = [
    path('licitaciones/', LicitacionListView.as_view(), name='list-licitaciones'),
    path('tdrs/', TDRListView.as_view(), name='list-tdrs'),
    path('create/', LicitacionCreateView.as_view(), name='create-licitacion'),  # Cambio aquí
    path('update/<int:pk>/', LicitacionUpdateView.as_view(), name='update-licitacion'),
    path('delete/<int:pk>/', LicitacionDeleteView.as_view(), name='delete-licitacion'),
    path('licitaciones/<int:pk>/', LicitacionDetailView.as_view(), name='licitacion-detail'),

]
