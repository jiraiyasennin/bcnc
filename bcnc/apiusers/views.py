from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Vivienda
from .serializers import ViviendaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ViviendaFilter


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        if Vivienda.objects.filter(usuario=user).exists():
            return Response(
                {"error": "No se puede eliminar el usuario porque tiene viviendas asociadas."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().destroy(request, *args, **kwargs)



class ViviendaListCreateView(generics.ListCreateAPIView):
    queryset = Vivienda.objects.all()
    serializer_class = ViviendaSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ViviendaFilter

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class ViviendaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vivienda.objects.all()
    serializer_class = ViviendaSerializer
    permission_classes = [IsAuthenticated]
