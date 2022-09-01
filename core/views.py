from rest_framework.viewsets import ModelViewSet

from core.models import Categoria, Marca, Veiculo
from core.serializers import CategoriaSerializer, MarcaSerializer, VeiculoSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer