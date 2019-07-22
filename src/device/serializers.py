from rest_framework import serializers
from .models import Device, Miner


class DevSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id','public_key']

class MinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miner
        fields = ['partial']
