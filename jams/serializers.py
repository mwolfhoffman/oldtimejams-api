from jams.models import Jam, Event

from rest_framework import serializers

class JamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jam
        fields = ('id', 'name', 'city', 'state')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'date', 'time', 'description', 'jam')