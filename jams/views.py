from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly

from jams.models import Jam, Event
from django.shortcuts import get_object_or_404
from django.http import Http404
from jams.serializers import JamSerializer, EventSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

##########  JAMS  ###########################3
class JamList(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get(self, request, format=None):
        jams = Jam.objects.all()
        serializer = JamSerializer(jams, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jam = self.get_object(pk)
        jam.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class JamDetail(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get_object(self, pk):
        try:
            return Jam.objects.get(pk=pk)
        except Jam.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        jam = self.get_object(pk)
        jam = JamSerializer(jam)
        return Response(jam.data)

    def put(self, request, pk, format=None):
        jam = self.get_object(pk)
        serializer = JamSerializer(jam, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jam = self.get_object(pk)
        jam.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

########################################################

###########  Events ###########

class EventList(APIView):
    def get(self, request, format=None):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EventDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        event = EventSerializer(event)
        return Response(event.data)

    def put(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#################################