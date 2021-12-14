
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.patients import PatientSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..models.patients import Patient

# Create your views here.


class PatientsView(APIView):
    def get(self, index):
        patient = Patient.objects.all()
        data = PatientSerializer(patient, many=True).data
        return Response(data)

    def post(self, request):
        patient = PatientSerializer(data=request.data)
        if patient.is_valid():
            patient.save()
            return Response(patient.data, status=status.HTTP_201_CREATED)
        else:
            return Response(patient.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientView(APIView):
    # GET /patients/:id
    def get(self, response, pk):
        patient = get_object_or_404(Patient, pk=pk)
        data = PatientSerializer(patient).data
        return Response(data)

    def delete(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        updated_patient = PatientSerializer(patient, data=request.data)
        if updated_patient.is_valid():
            updated_patient.save()
            return Response(updated_patient.data)

    def put(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        updated_patient = PatientSerializer(
            patient, data=request.data, partial=True)
        if updated_patient.is_valid():
            updated_patient.save()
            return Response(updated_patient.data)
