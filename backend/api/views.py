from django.shortcuts import render

from .models import DetailsCOE
from .serializers import all_Crtf_Serializer,Other_Crtf_Serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework import viewsets


#for students... get by rollnumber

class StudentListCreate(ListCreateAPIView):
    queryset = DetailsCOE.objects.all()
    serializer_class = all_Crtf_Serializer

class StudentRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = DetailsCOE.objects.all()
    serializer_class = all_Crtf_Serializer
    lookup_field = 'rollnumber'

    def retrieve(self, request, *args, **kwargs):
        rollnumber = kwargs.get('rollnumber')
        queryset = self.get_queryset().filter(rollnumber=rollnumber)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class facultyViewset(viewsets.ModelViewSet):
    queryset = DetailsCOE.objects.all()
    serializer_class = all_Crtf_Serializer
    def get_queryset(self):
        user = self.request.user
        return DetailsCOE.objects.filter(verified_by = user)