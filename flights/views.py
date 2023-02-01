from datetime import datetime

from rest_framework.generics import ListAPIView , RetrieveAPIView , UpdateAPIView , DestroyAPIView

from .models import Booking, Flight
from .serializers import BookingListSerializer, FlightListSerializer ,DetailSerializer, UpdateSerializer , DeleteSerializer


class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer


class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gte=datetime.today())
    serializer_class = BookingListSerializer

class DetialView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = DetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'

class UpdateBookingViews(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = UpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'

class DeleteBookingViews(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = DeleteSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'



