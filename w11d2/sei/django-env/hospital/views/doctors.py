import hospital
from housing.serializers.dorms import DormSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.doctors import DoctorSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..models.doctors import Doctor

# Create your views here.

class HospitalsView(APIView):
    def get(self, index):
        hospital = Doctor.objects.all()
        data = DoctorSerializer(hospital, many = True).data
        return Response(data)

    def post(self, request):
        hospital = DoctorSerializer(data = request.data)
        if hospital.is_valid():
            hospital.save()
            return Response(hospital.data, status=status.HTTP_201_CREATED)
        else:
            return Response(hospital.errors, status=status.HTTP_400_BAD_REQUEST)


class HospitalView(APIView):
    # GET /hospitals/:id
    def get(self, response, pk):
        hospital = get_object_or_404(Doctor, pk=pk)
        data = DoctorSerializer(hospital).data
        return Response(data)
    
    def delete(self, request, pk):
        hospital = get_object_or_404(Doctor, pk=pk)
        hospital.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        hospital = get_object_or_404(Doctor, pk=pk)
        updated_hospital = DoctorSerializer(hospital, data=request.data)
        if updated_hospital.is_valid():
            updated_hospital.save()
            return Response(updated_hospital.data)

    def put(self, request, pk):
        hospital = get_object_or_404(Doctor, pk=pk)
        updated_hospital = DoctorSerializer(hospital, data=request.data, partial = True)
        if updated_hospital.is_valid():
            updated_hospital.save()
            return Response(updated_hospital.data)
