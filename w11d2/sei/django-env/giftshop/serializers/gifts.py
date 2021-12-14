from rest_framework import serializers
from ..models.gitfts import Gift

class GiftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gift
        fields = "__all__"