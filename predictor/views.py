from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TurnoverSerializer
from .models import Turnover


# Create your views here.
class TurnoverViewset(viewsets.ModelViewSet):
    queryset = Turnover.objects.all()
    serializer_class = TurnoverSerializer
