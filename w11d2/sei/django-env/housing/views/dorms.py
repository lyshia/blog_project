from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.dorms import DormSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.
from ..models.dorms import Dorm


class DormsView(APIView):
    def get(self, request):
        dorms = Dorm.objects.all()
        data = DormSerializer(dorms, many = True).data
        return Response(data)

    def post(self, request):
        dorm = DormSerializer(data = request.data)
        if dorm.is_valid():
            dorm.save()
            return Response(dorm.data, status=status.HTTP_201_CREATED)
        else:
            return Response(dorm.errors, status=status.HTTP_400_BAD_REQUEST)

class DormView(APIView):
    def get(self, request, pk):
        dorm = get_object_or_404(Dorm, pk=pk)
        data = DormSerializer(dorm).data
        return Response(data)
        
    def delete(self, request, pk):
        dorm = get_object_or_404(Dorm, pk=pk)
        dorm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # def patch(self, request, pk):
    #     dorm = get_object_or_404(Dorm, pk=pk)
    #     updated_dorm = DormSerializer(dorm, data=request.data)
    #     if updated_dorm.is_valid():
    #         updated_dorm.save()
    #         return Response(updated_dorm.data)

    def patch(self, request, pk):
        dorm = get_object_or_404(Dorm, pk=pk)
        updated_dorm = DormSerializer(dorm, data=request.data)
        if updated_dorm.is_valid():
            updated_dorm.save()
            return Response(updated_dorm.data)

    def put(self, request, pk):
        dorm = get_object_or_404(Dorm, pk=pk)
        updated_dorm = DormSerializer(dorm, data=request.data, partial = True)
        if updated_dorm.is_valid():
            updated_dorm.save()
            return Response(updated_dorm.data)