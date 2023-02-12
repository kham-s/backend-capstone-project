from rest_framework.viewsets import ModelViewSet
from restaurant.models import Booking, Menu
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated

class BookingsViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class MenusViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]