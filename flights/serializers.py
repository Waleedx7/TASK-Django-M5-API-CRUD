from rest_framework import serializers
from .models import Booking, Flight


class FlightListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ["id", "price", "time", "destination"]


class BookingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "date", "flight"]

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id","flight","date","passengers"]

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking 
        fields = ["passengers","date"]

class DeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking 
        fields = ["id"]
        
