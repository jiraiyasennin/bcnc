import django_filters
from .models import Vivienda

class ViviendaFilter(django_filters.FilterSet):
    ciudad = django_filters.CharFilter(field_name='ciudad', lookup_expr='icontains')
    calle = django_filters.CharFilter(field_name='calle', lookup_expr='icontains')
    pais = django_filters.CharFilter(field_name='pais', lookup_expr='icontains')

    class Meta:
        model = Vivienda
        fields = ['ciudad', 'calle', 'pais']
