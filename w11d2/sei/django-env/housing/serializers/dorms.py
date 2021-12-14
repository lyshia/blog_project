from rest_framework import serializers
from ..models.dorms import  Dorm

class DormSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dorm
        fields = "__all__"