from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestroyView
from .views import ViviendaListCreateView, ViviendaRetrieveUpdateDestroyView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    path('viviendas/', ViviendaListCreateView.as_view(), name='vivienda-list-create'),
    path('viviendas/<int:pk>/', ViviendaRetrieveUpdateDestroyView.as_view(), name='vivienda-detail'),
]