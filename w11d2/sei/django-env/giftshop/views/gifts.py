from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.gifts import GiftSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..models.gitfts import Gift

class GiftsView(APIView):
    def get(self, request):
        gift = Gift.objects.all()
        data = GiftSerializer(gift, many=True).data
        return Response(data)

    def post(self, request):
        gift = GiftSerializer(data =request.data)
        if gift.is_valid():
            gift.save()
            return Response(gift.data, status=status.HTTP_201_CREATED)
        else:
            return Response(gift.errors, status=status.HTTP_400_BAD_REQUEST)


class GiftView(APIView):
    def get(self,request, pk):
        gift = get_object_or_404(Gift, pk=pk)
        data = GiftSerializer(gift).data
        return Response(data)

    def delete(self,request, pk):
        gift = get_object_or_404(Gift, pk=pk)
        gift.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        gift = get_object_or_404(Gift, pk=pk)
        data = GiftSerializer(gift, data = request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        return Response(gift.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        gift = get_object_or_404(Gift, pk=pk)
        updated_book = GiftSerializer(gift, data=request.data)
        if updated_book.is_valid():
            updated_book.save()
            return Response(updated_book.data)
