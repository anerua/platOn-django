from datetime import date
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from .models import Event
from .serializers import EventSerializer

class EventAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.filter(start__gte = date.today())
    serializer_class = EventSerializer
    permission_classes = (IsAdminUser,)   
    
class EventAllAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAdminUser,)   
    