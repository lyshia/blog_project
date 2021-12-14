from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.foods import FoodSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.

from ..models.foods import Food
class CafeteriasView(APIView):
    def get(self, request):
        food = Food.objects.all()
        data = FoodSerializer(food, many = True).data
        return Response(data)   

    def post(self, request):
        food = FoodSerializer(data = request.data)
        if food.is_valid():
            food.save()
            return Response(food.data, status=status.HTTP_201_CREATED)
        else:
            return Response(food.errors, status=status.HTTP_400_BAD_REQUEST)

class CafeteriaView(APIView):
    def get(show, request, pk):
        food = get_object_or_404(Food, pk=pk)
        data = FoodSerializer(food).data
        return Response(data)

    def delete(self, request, pk):
        food = get_object_or_404(Food, pk=pk)
        food.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        food = get_object_or_404(Food, pk=pk)
        updated_food = FoodSerializer(food, data=request.data)
        if updated_food.is_valid():
            updated_food.save()
            return Response(updated_food.data)

    def put(self, request, pk):
        food = get_object_or_404(Food, pk=pk)
        updated_food = FoodSerializer(food, data=request.data, partial=True)
        if updated_food.is_valid():
            updated_food.save()
            return Response(updated_food.data)
