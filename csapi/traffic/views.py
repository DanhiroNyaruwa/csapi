from django.shortcuts import render
from .models import AADF
from rest_framework import generics
from traffic.serializers import AADFSerializer


class AADFList(generics.ListCreateAPIView):
    queryset = AADF.objects.all()
    serializer_class = AADFSerializer
    filter_fields = ('CP', 'AADFYEAR','Region','Road', 'RoadCategory','LocalAuthority')

#class AADFDetails(generics.RetrieveUpdateDestroyAPIView):
#    queryset = AADF.objects.all()
#    serializer_class = AADFSerializer

