from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Car
from .serializers import CarSerializer


# Create your views here.
class CarsList(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarsDetail(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer