from rest_framework import viewsets
from rest_framework import mixins

from usuarios.models import User
from usuarios.apis.serializers import UserSerializer

class UsuarioListCreate(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAdminUser]