from rest_framework import serializers
from myweb.models import VID
class VIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = VID
        fields ='__all__'